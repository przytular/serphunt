from django.test import TestCase, Client
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from unittest import skip
from django.core.management import call_command


class SpoofTestCase(TestCase):

	@classmethod
	def setUpTestData(cls):
		cls.client = Client()
		cls.user_data = {'username': 'testuser', 'password': 'test1234', 'is_active': True}
		cls.user = User.objects.create(**cls.user_data)

	@skip('external website down')
	def test_user_agents_scraper(self):
		" Test user agents scraper"
		call_command('scrape_user_agents')

	def test_new_proxies_can_be_added(self):
		data = {
			'new_proxies': 'proxy-user_485e:proxy_pass!@#%*(@127.0.0.1:8001\nproxy_user_393:pass&*$@127.0.0.1:8002'
		}
		response = self.client.post(reverse_lazy('proxies'), data=data)

	def test_history_page_is_available_only_for_logged_in_users(self):
		response = self.client.get(reverse_lazy('history'))
		self.assertEqual(response.status_code, 302)
		self.client.force_login(user=self.user)
		response = self.client.get(reverse_lazy('history'))
		self.assertEqual(response.status_code, 200)
