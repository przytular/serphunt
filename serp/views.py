from django.shortcuts import render
from django.views.generic.edit import FormView
from rest_framework import viewsets, mixins
from rest_framework.response import Response

from .models import SearchResults
from .serializers import SearchResultsSerializer
from .permissions import OwnedSearchResult
from .forms import SearchForm


class IndexView(FormView):
	template_name = 'index.html'
	form_class = SearchForm


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
		# serp_results = get_google_results(data['keyword'])

		data['ip'] = request.META.get('HTTP_X_FORWARDED_FOR')
		data['results'] = None
		serializer = self.serializer_class(data=data)
		if serializer.is_valid():
			obj = serializer.save()
		breakpoint()
		return Response(obj)
