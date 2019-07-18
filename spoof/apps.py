from django.apps import AppConfig


class SpoofConfig(AppConfig):
    name = 'spoof'

    def ready(self):
        import serphunt.serp.signals