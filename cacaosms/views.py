# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .models import Bitacora

@method_decorator(csrf_exempt, name='dispatch')
class StatusCallBack(View):

    def post(self, request, *args, **kwargs):
        print request
        print request.POST
        #entrada = Bitacora()
        #entrada.save()
        return HttpResponse('')
