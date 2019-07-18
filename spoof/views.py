import datetime
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from rest_framework import viewsets, mixins
from rest_framework.response import Response
from .models import Proxy
from .forms import AddProxiesForm
from .serializers import ProxySerializer
from .helpers import parse_new_proxies


@method_decorator(login_required, name='dispatch')
class ProxyView(FormView):
	template_name = 'spoof/proxies.html'
	form_class = AddProxiesForm
	success_url = reverse_lazy('proxies')


@method_decorator(login_required, name='dispatch')
class ProxyViewSet(viewsets.GenericViewSet,
					mixins.CreateModelMixin,
					mixins.ListModelMixin,
					mixins.DestroyModelMixin):
	queryset = Proxy.objects.all()
	serializer_class = ProxySerializer


	def create(self, request, *args, **kwargs):
		data = request.data.dict()
		new_proxies = data.get('new_proxies')
		new_proxies = parse_new_proxies(new_proxies)
		objects = []
		for proxy in new_proxies:
			user_pk = request.user.pk if request.user.is_authenticated else None
			proxy['user'] = user_pk
			serializer = self.serializer_class(data=proxy)
			if serializer.is_valid():
				obj = serializer.save()
				proxy_url = url = obj.get_proxy_url()
				objects.append(serializer.data)
			else:
				pass
		return Response(objects)
