"""_core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from rest_framework.routers import DefaultRouter

from serp.views import SearchViewSet

router = DefaultRouter()
router.register(r'search', SearchViewSet)

urlpatterns = [
	path('', TemplateView.as_view(template_name='index.html'), name='home'),
	path('history/', TemplateView.as_view(template_name='history.html'), name='history'),

    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),

    path('admin/', admin.site.urls),
]
