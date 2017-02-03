# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 19:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cacaosms', '0007_auto_20170203_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='bitacora',
            name='de_numero',
            field=models.CharField(default=0, max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bitacora',
            name='para_numero',
            field=models.CharField(default=0, max_length=32),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bitacora',
            name='de',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='bitacora',
            name='envio_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bitacora',
            name='estado',
            field=models.CharField(default=b'nuevo', max_length=64),
        ),
        migrations.AlterField(
            model_name='bitacora',
            name='fecha_envio',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='bitacora',
            name='para',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='envios',
            name='estado',
            field=models.CharField(choices=[(b'N', b'Nuevo'), (b'P', b'Programado'), (b'S', b'Enviado'), (b'I', b'En Proceso'), (b'E', b'Error')], max_length=1),
        ),
    ]