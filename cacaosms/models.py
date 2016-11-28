# -*- coding: utf-8 -*-

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext as _


@python_2_unicode_compatible
class ContactoTipo(models.Model):

    nombre = models.CharField(max_length=100, verbose_name=u"Nombre")
    

    class Meta:
        ordering = ['nombre',]
        verbose_name = _(u'ContactoTipo')
        verbose_name_plural = _(u'ContactoTipo')

    
    def __str__(self):
        return "%s " % (self.nombre, )
    


@python_2_unicode_compatible
class Pais(models.Model):

    nombre = models.CharField(max_length=100, verbose_name=u"Nombre")
    codigo = models.IntegerField(verbose_name=u"Código telefónico")
    

    class Meta:
        ordering = ['nombre',]
        verbose_name = _(u'Pais')
        verbose_name_plural = _(u'Pais')

    
    def __str__(self):
        return "%s " % (self.nombre, )
    


@python_2_unicode_compatible
class Grupo(models.Model):

    nombre = models.CharField(max_length=100, verbose_name=u"Nombre")
    

    class Meta:
        ordering = ['nombre',]
        verbose_name = _(u'Agrupación')
        verbose_name_plural = _(u'Agrupación')

    
    def __str__(self):
        return "%s " % (self.nombre, )
    


@python_2_unicode_compatible
class Bitacora(models.Model):

    de = models.IntegerField()
    para = models.IntegerField()
    mensaje = models.CharField(max_length=160)
    fecha = models.DateTimeField()
    

    class Meta:
        ordering = []
        verbose_name = _(u'Bitacora')
        verbose_name_plural = _(u'Bitacora')

    
    def __str__(self):
        return "%s %s %s " % (self.de, self.para, self.fecha, )
    


@python_2_unicode_compatible
class Respuesta(models.Model):

    nombre = models.CharField(max_length=160)
    mensaje = models.CharField(max_length=160, verbose_name=u"Mensaje de respuesta")
    

    class Meta:
        ordering = ['nombre',]
        verbose_name = _(u'Respuesta')
        verbose_name_plural = _(u'Respuesta')

    
    def __str__(self):
        return "%s " % (self.nombre, )
    


@python_2_unicode_compatible
class Trivia(models.Model):

    nombre = models.CharField(max_length=160)
    

    class Meta:
        ordering = ['nombre',]
        verbose_name = _(u'Trivia')
        verbose_name_plural = _(u'Trivia')

    
    def __str__(self):
        return "%s " % (self.nombre, )
    


@python_2_unicode_compatible
class Estado(models.Model):

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    

    class Meta:
        ordering = ['nombre',]
        verbose_name = _(u'Estado de envío')
        verbose_name_plural = _(u'Estado de envío')

    
    def __str__(self):
        return "%s " % (self.nombre, )
    


@python_2_unicode_compatible
class Contacto(models.Model):

    nombre = models.CharField(max_length=200, verbose_name=u"Nombre")
    telefono = models.IntegerField(verbose_name=u"Teléfono")
    pais = models.ForeignKey(Pais, verbose_name=u"País")
    contactotipo = models.ForeignKey(ContactoTipo, null=True, blank=True, verbose_name=u"Tipo")
    grupo = models.ForeignKey(Grupo, null=True, blank=True, verbose_name=u"Grupo")
    recibidos = models.IntegerField(null=True, blank=True)
    

    class Meta:
        ordering = ['nombre',]
        verbose_name = _(u'Contacto')
        verbose_name_plural = _(u'Contacto')

    
    def __str__(self):
        return "%s %s " % (self.nombre, self.telefono, )
    


@python_2_unicode_compatible
class Mensaje(models.Model):

    nombre = models.CharField(max_length=100)
    mensaje = models.CharField(max_length=160)
    enviados = models.IntegerField(null=True, blank=True)
    

    class Meta:
        ordering = ['nombre',]
        verbose_name = _(u'Mensaje')
        verbose_name_plural = _(u'Mensaje')

    
    def __str__(self):
        return "%s " % (self.nombre, )
    


@python_2_unicode_compatible
class Envios(models.Model):

    de = models.CharField(max_length=100, verbose_name=u"Quién envía")
    para_pais = models.ForeignKey(Pais, null=True, blank=True, verbose_name=u"Para todo un país")
    para_contactotipo = models.ForeignKey(ContactoTipo, null=True, blank=True, verbose_name=u"Para todo un tipo de contacto")
    para_contacto = models.ForeignKey(Contacto, null=True, blank=True, verbose_name=u"Para un número específico")
    para_grupo = models.ForeignKey(Grupo, null=True, blank=True, verbose_name=u"Para un grupo")
    texto = models.CharField(max_length=160, null=True, blank=True, verbose_name=u"Mensaje personalizado")
    mensaje = models.ForeignKey(Mensaje, null=True, blank=True, verbose_name=u"Mensaje")
    finalizada = models.DateTimeField(null=True, blank=True, verbose_name=u"Fecha real finalizada")
    programada = models.DateTimeField(verbose_name=u"Fecha programada")
    envios_programados = models.IntegerField(null=True, blank=True)
    envios_realizados = models.IntegerField(null=True, blank=True)
    estado = models.CharField(max_length=1, choices=(('N', 'Nuevo'), ('P', 'Programado'), ('E', 'Enviado'), ('I', 'En Proceso')))
    

    class Meta:
        ordering = []
        verbose_name = _(u'Envíos')
        verbose_name_plural = _(u'Envíos')

    
    def __str__(self):
        return "%s " % (self.de, )
    


