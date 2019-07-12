from django.shortcuts import render
from rest_framework import viewsets, mixins

from .models import SearchResults
from .serializers import SearchResultsSerializer


class SearchViewSet(viewsets.GenericViewSet,
					mixins.CreateModelMixin,
					mixins.RetrieveModelMixin):
	""" Viewset for handling search requests and returning results.
	"""
	queryset = SearchResults.objects.all()
	serializer_class = SearchResultsSerializer
