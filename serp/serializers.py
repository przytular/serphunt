from rest_framework import serializers

from .models import SearchResults


class SearchResultsSerializer(serializers.ModelSerializer):
	class Meta:
		model = SearchResults
		fields = '__all__'
