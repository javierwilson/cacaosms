from django.apps import AppConfig

class CacaoSMSAppConfig(AppConfig):

    name = 'cacaosms'
    verbose_name = 'Cacao SMS'

    def ready(self):
        import cacaosms.signals
