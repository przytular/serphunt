from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from serp.views import IndexView, HistoryView, SearchViewSet, UserConfigView
from spoof.views import ProxyView, ProxyViewSet

router = DefaultRouter()
router.register(r'keywords', SearchViewSet, basename='keywords')
router.register(r'proxies', ProxyViewSet, basename='proxies')

urlpatterns = [
	path('', IndexView.as_view(), name='home'),
	path('history/', HistoryView.as_view(), name='history'),
	path('config/', UserConfigView.as_view(), name='config'),
	path('proxies/', ProxyView.as_view(), name='proxies'),

	path('accounts/', include('allauth.urls')),

    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
]
