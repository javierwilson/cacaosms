# -*- coding: utf-8 -*-

from datetime import datetime

from django.http import HttpResponse
from django.views import View
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from cacaosms.taskapp.celery import send_sms
from .models import Bitacora, Respuesta


@method_decorator(csrf_exempt, name='dispatch')
class StatusCallBack(DetailView):
    model = Bitacora

    def post(self, request, *args, **kwargs):
        # <QueryDict: {u'MessageSid': [u'SM98c5c5e8711a4334b678c0411d3f718d'], u'SmsStatus': [u'delivered'], u'ApiVersion': [u'2010-04-01'], u'To': [u'+50588842452'], u'From': [u'+14439571255'], u'MessageStatus': [u'delivered'], u'AccountSid': [u'AC796070dfd05fcc12f9a99e504c5017bd'], u'SmsSid': [u'SM98c5c5e8711a4334b678c0411d3f718d']}>
        self.object = self.get_object()
        self.object.estado = 'resultado'
        self.object.fecha_resultado = datetime.now()
        self.object.resultado = request.POST.get('MessageStatus')
        self.object.save()
        return HttpResponse('')

@method_decorator(csrf_exempt, name='dispatch')
class ReplyWebHook(View):

    def post(self, request, *args, **kwargs):
        ret = ''
        respuesta = None
        print request.POST
        message = request.POST.get('Body')
        para = request.POST.get('From')
        if not message or not para:
            ret = "No message or from"
            return HttpResponse(ret)
        try:
            respuesta = Respuesta.objects.get(nombre=message.lower())
        except Respuesta.DoesNotExist:
            print "%s does not exist" % (message,)
            ret = "%s does not exist" % (message,)
            return HttpResponse(ret)
        print "%s: %s" % (para, respuesta.mensaje)
        task = send_sms.delay(para, respuesta.mensaje)
        if task:
            print task.status
        return HttpResponse(ret)
