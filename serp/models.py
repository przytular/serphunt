from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField


class UserConfig(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	time_limit = models.IntegerField(default=300)


class SearchResults(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	created = models.DateTimeField(auto_now_add=True)
	ip = models.GenericIPAddressField()
	keyword = models.CharField(max_length=255)
	results = JSONField()
