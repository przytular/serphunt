import json
import requests
import string
import urllib.parse
from django.utils.http import urlquote
from bs4 import BeautifulSoup as bs
from collections import Counter


def get_google_results(keyword):
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0'
	}

	r = requests.get('https://www.google.com/search?q={}'.format(urllib.parse.quote_plus(keyword),), headers=headers)

	soup = bs(r.text, 'html.parser')
	stats = soup.find('div', {'id': 'resultStats'}).text
	stats = stats[:stats.find('(')]
	stats = "".join([ char for char in stats if char.isdigit()])

	serp = []
	result_divs = soup.findAll('div', {'class': 'rc'})

	all_text = ""

	for i, r in enumerate(result_divs, 1):
		title = r.find('h3').text
		desc = r.find('div', {'class': 's'}).text
		site = r.find('cite').text
		serp.append([i, "<b>{0}</b><br/><small><a href='{1}'>{1}</a><br/><p>{2}</small>".format(title, site, desc)])
		all_text += " "+title+" "+desc

	# Make list of words and clean it from punctuation. Remove words shorter than 3 letters
	all_words = all_text.split()
	all_words_clean = [ s.translate(str.maketrans('', '', string.punctuation)) for s in all_words ]
	all_words_clean = list(filter(None, all_words_clean))
	all_words_clean = [ word.lower() for word in all_words_clean if len(word) >= 3 ]
	popular = Counter(all_words_clean).most_common(10)

	return json.dumps({
		'stats': stats,
		'serp': serp,
		'popular': popular
	})
