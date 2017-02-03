# -*- coding: utf-8 -*-

from datetime import datetime

from django.http import HttpResponse
from django.views import View
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .models import Bitacora


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
