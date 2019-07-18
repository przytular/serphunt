from django.core.management.base import BaseCommand
from django.utils import timezone

from spoof.models import UserAgent

import requests
from bs4 import BeautifulSoup


class Command(BaseCommand):
	help = 'Scrape actual user agents for browsers from useragentstring.com'

	def handle(self, *args, **kwargs):
		website = 'http://useragentstring.com'
		ua = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0'
		headers = { 'User-Agent': ua }
		r = requests.get("{}{}".format(website, "/pages/useragentstring.php"), headers=headers)
		soup = BeautifulSoup(r.text, 'html')
		browsers_section = [ x for x in soup.findAll('a', {'class': 'unterMenuTitel'}) if x.text == 'BROWSERS'][0]
		a_links = browsers_section.parent.findAll('a', {'class': 'unterMenuName'})
		for link in a_links:
			browser_name = link.text
			r = requests.get('{}{}'.format(website, link['href']))
			soup = BeautifulSoup(r.text, 'html')
			ua_string = soup.find('div', {'id': 'liste'}).select('ul li a')[0].text
			UserAgent.objects.create(browser=browser_name, string=ua_string)