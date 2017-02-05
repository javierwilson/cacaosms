# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^api/status/(?P<pk>\d+)/$', views.StatusCallBack.as_view(), name='api-status'),
    url(r'^api/reply/$', views.ReplyWebHook.as_view(), name='api-reply'),
]
