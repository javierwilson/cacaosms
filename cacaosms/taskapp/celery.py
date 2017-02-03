
from __future__ import absolute_import
import os
from celery import Celery
from django.apps import apps, AppConfig
from django.conf import settings



if not settings.configured:
    # set the default Django settings module for the 'celery' program.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')  # pragma: no cover


app = Celery('cacaosms', broker='redis://localhost:6379/0')


class CeleryConfig(AppConfig):
    name = 'cacaosms.taskapp'
    verbose_name = 'Celery Config'

    def ready(self):
        # Using a string here means the worker will not have to
        # pickle the object when using Windows.
        app.config_from_object('django.conf:settings', namespace='CELERY')
        #installed_apps = [app_config.name for app_config in apps.get_app_configs()]
        #app.autodiscover_tasks(lambda: installed_apps, force=True)
        app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))  # pragma: no cover

@app.task
def add(x, y):
    return x + y


from twilio.rest import TwilioRestClient

@app.task
def send_sms(phone_number_to, message, from_str=None, to_str=None, id_str=None):
    from cacaosms.models import Bitacora
    account_sid = settings.SMS_ACCOUNT_SID
    auth_token = settings.SMS_AUTH_TOKEN
    phone_number_from = settings.SMS_PHONE_NUMBER
    status_callback = settings.SMS_STATUS_CALLBACK

    if from_str and to_str and id_str:
        entrada = Bitacora(de=from_str, para=to_str, de_numero=phone_number_from, para_numero=phone_number_to, envio_id=id_str, mensaje=message)
    else:
        entrada = Bitacora(de_numero=phone_number_from, para_numero=phone_number_to, mensaje=message)
    entrada.save()

    client = TwilioRestClient(account_sid, auth_token)
    message = client.messages.create(to=phone_number_to, from_=phone_number_from, body=message, status_callback=status_callback)
