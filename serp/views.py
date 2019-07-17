import datetime
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.conf import settings

from rest_framework import viewsets, mixins
from rest_framework.response import Response

from .models import SearchResults, UserConfig
from .serializers import SearchResultsSerializer
from .permissions import OwnedSearchResult
from .forms import SearchForm, UserConfigForm, HistoryForm
from .helpers import get_google_results


class IndexView(FormView):
	template_name = 'index.html'
	form_class = SearchForm


@method_decorator(login_required, name='dispatch')
class HistoryView(FormView):
	# TODO: Clear history
	template_name = 'history.html'
	form_class = HistoryForm

	def get_form_kwargs(self):
		kwargs = super().get_form_kwargs()
		kwargs['user'] = self.request.user
		return kwargs


@method_decorator(login_required, name='dispatch')
class UserConfigView(UpdateView):
	template_name = 'config.html'
	model = UserConfig
	form_class = UserConfigForm
	success_url = reverse_lazy('config')

	def get_object(self):
		return self.model.objects.filter(user=self.request.user).first()


class SearchViewSet(viewsets.GenericViewSet,
					mixins.CreateModelMixin,
					mixins.RetrieveModelMixin):
	""" Viewset for handling search requests and returning results.
	"""
	queryset = SearchResults.objects.all()
	serializer_class = SearchResultsSerializer
	permission_classes = (OwnedSearchResult,)

	def create(self, request, *args, **kwargs):
		data = request.data.dict()
		keyword = data.get('keyword')
		user = request.user if request.user.is_authenticated else None
		if request.user.is_authenticated:
			data['user'] = user.pk
			scraper_limit_time = user.config.time_limit
		else:
			scraper_limit_time = settings.SERP_SCRAPER_TIME_LIMIT

		# Check if search results already exists and check scraper time limit.
		sr = SearchResults.objects.filter(
			keyword=keyword,
			user=user)
		try:
			sr = sr.latest()
			time_limit = sr.created + datetime.timedelta(seconds=scraper_limit_time)
			if datetime.datetime.now() < time_limit:
				serializer = self.serializer_class(sr)
				return Response(serializer.data)
		except SearchResults.DoesNotExist:
			pass

		# Update serializer data dictionary with results and user IP
		data.update({'ip': request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR', '127.0.0.1'))})
		data.update({"results": get_google_results(keyword)} if keyword else {"results": ""})

		serializer = self.serializer_class(data=data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors, status=400)
