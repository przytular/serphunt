from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from rest_framework.routers import DefaultRouter

from serp.views import SearchViewSet

router = DefaultRouter()
router.register(r'keywords', SearchViewSet)

urlpatterns = [
	path('', TemplateView.as_view(template_name='index.html'), name='home'),
	path('history/', TemplateView.as_view(template_name='history.html'), name='history'),

    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),

    path('admin/', admin.site.urls),
]
