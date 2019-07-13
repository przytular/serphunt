from django.contrib import admin

from .models import UserConfig, SearchResults

admin.site.register(UserConfig)
admin.site.register(SearchResults)
