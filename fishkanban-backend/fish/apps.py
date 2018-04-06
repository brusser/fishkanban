from django.apps import AppConfig


class FishConfig(AppConfig):
    name = 'fish'

    def ready(self):
        import fish.signals
