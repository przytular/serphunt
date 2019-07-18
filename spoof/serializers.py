from rest_framework import serializers

from django.conf import settings
from django.template.loader import render_to_string
from .models import Proxy


class ProxySerializer(serializers.ModelSerializer):
	proxy_url = serializers.SerializerMethodField()
	proxy_buttons = serializers.SerializerMethodField()

	class Meta:
		model = Proxy
		fields = '__all__'

	def get_proxy_url(self, obj):
		return obj.get_proxy_url()

	def get_proxy_buttons(self, obj):
		return render_to_string('spoof/proxy_table_row.html', {
			'pk': obj.pk
		})