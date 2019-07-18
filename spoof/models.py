from django.db import models


class Proxy(models.Model):
	ip = models.GenericIPAddressField(null=True, blank=True)
	port = models.SmallIntegerField(default=8080)
	user = models.CharField(max_length=30)
	password = models.CharField(max_length=30)


class UserAgent(models.Model):
	browser = models.CharField(max_length=150)
	string = models.CharField(max_length=255)

	class Meta:
		ordering = ['browser']

	def __str__(self):
		return self.browser
