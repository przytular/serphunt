from django.test import TestCase, Client
from django.urls import reverse_lazy
from django.contrib.auth.models import User


class SERPTestCase(TestCase):

	@classmethod
	def setUpTestData(cls):
		cls.client = Client()
		cls.user_data = {'username': 'testuser', 'password': 'test1234', 'is_active': True}
		cls.user = User.objects.create(**cls.user_data)

	def test_home_page_is_available_for_everyone(self):
		response = self.client.get(reverse_lazy('home'))
		self.assertEqual(response.status_code, 200)

	def test_history_page_is_available_only_for_logged_in_users(self):
		response = self.client.get(reverse_lazy('history'))
		self.assertEqual(response.status_code, 302)
		self.client.force_login(user=self.user)
		response = self.client.get(reverse_lazy('history'))
		self.assertEqual(response.status_code, 200)

	def test_everybody_can_make_a_request_to_api(self):
		data = {
			'keyword': 'kaszmirowa sukienka'
		}
		response = self.client.post(reverse_lazy('keywords-list'), data=data)
		self.assertIn('results', response.json())
		self.assertEqual(response.status_code, 200)

	def test_no_keyword_provided_gives_error(self):
		data = {}
		response = self.client.post(reverse_lazy('keywords-list'), data=data)
		self.assertEqual(response.status_code, 400)
		self.assertIn('keyword', response.json())
