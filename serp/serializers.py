from rest_framework import serializers

from django.conf import settings
from .models import SearchResults


class SearchResultsSerializer(serializers.ModelSerializer):
	cache = serializers.BooleanField(default=False, read_only=True)
	user_agent = serializers.SerializerMethodField()

	class Meta:
		model = SearchResults
		fields = '__all__'

	def get_user_agent(self, obj):
		user_ua = obj.user.config.user_agent if obj.user else None
		return user_ua.string if user_ua else settings.DEFAULT_UA
