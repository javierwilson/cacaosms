# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-28 17:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cacaosms', '0004_auto_20161128_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bitacora',
            name='de',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='bitacora',
            name='fecha',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='bitacora',
            name='mensaje',
            field=models.CharField(max_length=160),
        ),
        migrations.AlterField(
            model_name='bitacora',
            name='para',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='recibidos',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='envios',
            name='envios_programados',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='envios',
            name='envios_realizados',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='envios',
            name='estado',
            field=models.CharField(choices=[(b'N', b'Nuevo'), (b'P', b'Programado'), (b'E', b'Enviado'), (b'I', b'En Proceso')], max_length=1),
        ),
        migrations.AlterField(
            model_name='estado',
            name='descripcion',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='estado',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='mensaje',
            name='enviados',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mensaje',
            name='mensaje',
            field=models.CharField(max_length=160),
        ),
        migrations.AlterField(
            model_name='mensaje',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='respuesta',
            name='nombre',
            field=models.CharField(max_length=160),
        ),
        migrations.AlterField(
            model_name='trivia',
            name='nombre',
            field=models.CharField(max_length=160),
        ),
    ]
