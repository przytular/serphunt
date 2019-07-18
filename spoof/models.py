from django.db import models
from django.contrib.auth.models import User


class Proxy(models.Model):
	host = models.GenericIPAddressField(null=True, blank=True)
	port = models.SmallIntegerField(default=8080)
	proxy_user = models.CharField(max_length=30, null=True, blank=True)
	password = models.CharField(max_length=30, null=True, blank=True)
	user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

	class Meta:
		unique_together = ('host', 'port')

	def get_proxy_url(self, scheme='http'):
		# http://USER:PASSWORD@HOST:PORT
		url = "{}://".format(scheme,)
		if self.user and self.password:
			url += "{}:{}@".format(self.user, self.password)
		url += "{}:{}".format(self.host, self.port)
		return url


class UserAgent(models.Model):
	browser = models.CharField(max_length=150)
	string = models.CharField(max_length=255)

	class Meta:
		ordering = ['browser']

	def __str__(self):
		return self.browser
