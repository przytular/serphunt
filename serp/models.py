from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from django.conf import settings

from spoof.models import UserAgent


class UserConfig(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='config')
	time_limit = models.IntegerField(default=settings.SERP_SCRAPER_TIME_LIMIT)
	user_agent = models.ForeignKey(UserAgent, on_delete=models.SET_NULL, null=True)
	use_proxy = models.BooleanField(default=False)


class SearchResults(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	created = models.DateTimeField(auto_now_add=True)
	ip = models.GenericIPAddressField()
	keyword = models.CharField(max_length=255)
	results = JSONField()

	class Meta:
		get_latest_by = 'created'

	def __str__(self):
		return "{} : {}".format(self.created.strftime(settings.DATETIME_FORMAT), self.keyword)
