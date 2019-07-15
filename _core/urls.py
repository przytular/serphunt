from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from serp.views import IndexView, HistoryView, SearchViewSet, UserConfigView

router = DefaultRouter()
router.register(r'keywords', SearchViewSet, basename='keywords')

urlpatterns = [
	path('', IndexView.as_view(), name='home'),
	path('history/', HistoryView.as_view(), name='history'),
	path('config/', UserConfigView.as_view(), name='config'),
	path('accounts/', include('allauth.urls')),

    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
]
