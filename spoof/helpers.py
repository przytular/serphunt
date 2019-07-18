import re
from .models import Proxy


def parse_new_proxies(string):
	data = []
	proxy_strings = string.splitlines()
	for s in proxy_strings:
		m = re.search(r'(http://)?([\w\d_\-\.]+:.{0,30}@)?([\d\.]+):(\d+)', s, re.IGNORECASE)
		if m:
			groups = m.groups()
			if groups[2] and groups[3]:
				data.append({'proxy_user': groups[0], 'password': groups[1], 'host': groups[2], 'port': groups[3]})
	return data
