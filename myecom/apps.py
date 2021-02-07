from django.apps import AppConfig


class MyecomConfig(AppConfig):
    name = 'myecom'

    def ready(self):
        import myecom.signal
