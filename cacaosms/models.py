# -*- coding: utf-8 -*-

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext as _



class Mensaje(models.Model):

    

    class Meta:
        ordering = []
        verbose_name = _(u'Mensaje')
        verbose_name_plural = _(u'Mensaje')

    



class Bitacora(models.Model):

    

    class Meta:
        ordering = []
        verbose_name = _(u'Bitacora')
        verbose_name_plural = _(u'Bitacora')

    



class Respuesta(models.Model):

    

    class Meta:
        ordering = []
        verbose_name = _(u'Respuesta')
        verbose_name_plural = _(u'Respuesta')

    



class Trivia(models.Model):

    

    class Meta:
        ordering = []
        verbose_name = _(u'Trivia')
        verbose_name_plural = _(u'Trivia')

    


@python_2_unicode_compatible
class ContactoTipo(models.Model):

    nombre = models.CharField(max_length=100, verbose_name=_(u'Nombre'))
    

    class Meta:
        ordering = ['nombre',]
        verbose_name = _(u'ContactoTipo')
        verbose_name_plural = _(u'ContactoTipo')

    
    def __str__(self):
        return "%s " % (self.nombre, )
    



class Envios(models.Model):

    

    class Meta:
        ordering = []
        verbose_name = _(u'Envios')
        verbose_name_plural = _(u'Envios')

    


@python_2_unicode_compatible
class Contacto(models.Model):

    pais = models.ForeignKey('Pais', verbose_name=_(u'País'))
    contactotipo = models.ForeignKey('ContactoTipo', verbose_name=_(u'Tipo'))
    nombre = models.CharField(max_length=200, verbose_name=_(u'Nombre'))
    telefono = models.IntegerField(verbose_name=_(u'Teléfono'))
    

    class Meta:
        ordering = ['nombre',]
        verbose_name = _(u'Contacto')
        verbose_name_plural = _(u'Contacto')

    
    def __str__(self):
        return "%s %s " % (self.nombre, self.telefono, )
    


@python_2_unicode_compatible
class Pais(models.Model):

    nombre = models.CharField(max_length=100, verbose_name=_(u'Nombre'))
    codigo = models.IntegerField(verbose_name=_(u'Código telefónico'))
    

    class Meta:
        ordering = ['nombre',]
        verbose_name = _(u'Pais')
        verbose_name_plural = _(u'Pais')

    
    def __str__(self):
        return "%s " % (self.nombre, )
    


