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
from .forms import SearchForm, UserConfigForm
from .helpers import get_google_results


class IndexView(FormView):
	template_name = 'index.html'
	form_class = SearchForm


@method_decorator(login_required, name='dispatch')
class HistoryView(TemplateView):
	template_name = 'history.html'


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
		data['user'] = user.pk

		# Check if search results already exists and check scraper time limit.
		sr = SearchResults.objects.filter(
			keyword=keyword,
			user=data['user'])
		sr = sr.latest()
		if sr:
			if request.user.is_authenticated:
				tl = user.config.time_limit
			else:
				tl = settings.SERP_SCRAPER_TIME_LIMIT
			time_limit = sr.created + datetime.timedelta(seconds=tl)
			if datetime.datetime.now() < time_limit:
				serializer = self.serializer_class(sr)
				return Response(serializer.data)

		# Update data dictionary with mandatory fields
		data['ip'] = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR', '127.0.0.1'))
		data.update({"results": get_google_results(keyword)} if keyword else {"results": ""})

		# Serializer validation and return.
		serializer = self.serializer_class(data=data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors, status=400)
