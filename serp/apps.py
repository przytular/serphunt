from django.apps import AppConfig


class SerpConfig(AppConfig):
    name = 'serp'

    def ready(self):
        import serphunt.serp.signals