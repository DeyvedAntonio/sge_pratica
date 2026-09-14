from django.apps import AppConfig


class InflowsConfig(AppConfig):
    name = "inflows"

    def ready(self) -> None:
        import inflows.signals
