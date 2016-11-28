from django.contrib import admin
from .models import *


class ContactoInline(admin.TabularInline):
    model = Contacto



admin.site.register(ContactoTipo)




class PaisAdmin(admin.ModelAdmin):
    list_display = ['nombre','codigo',]
    
    search_fields = ['nombre',]
    
    
    
    inlines = [
    
        ContactoInline,
    
    ]
    

admin.site.register(Pais, PaisAdmin)




class ContactoAdmin(admin.ModelAdmin):
    list_display = ['nombre','telefono','pais','contactotipo','grupo',]
    list_filter = ('pais','contactotipo','grupo',)
    search_fields = ['nombre','telefono',]
    
    list_per_page = 100
    

admin.site.register(Contacto, ContactoAdmin)




class GrupoAdmin(admin.ModelAdmin):
    list_display = ['nombre',]
    list_filter = ('nombre',)
    
    
    
    
    inlines = [
    
        ContactoInline,
    
    ]
    

admin.site.register(Grupo, GrupoAdmin)




class BitacoraAdmin(admin.ModelAdmin):
    list_display = ['de','para','mensaje','fecha',]
    list_filter = ('de','para','fecha',)
    
    
    
    

admin.site.register(Bitacora, BitacoraAdmin)




class MensajeAdmin(admin.ModelAdmin):
    list_display = ['nombre','mensaje',]
    
    
    
    
    

admin.site.register(Mensaje, MensajeAdmin)




class RespuestaAdmin(admin.ModelAdmin):
    list_display = ['nombre','mensaje',]
    
    
    
    
    

admin.site.register(Respuesta, RespuestaAdmin)




class TriviaAdmin(admin.ModelAdmin):
    list_display = ['nombre',]
    
    
    
    
    

admin.site.register(Trivia, TriviaAdmin)




class EnviosAdmin(admin.ModelAdmin):
    list_display = ['de','texto','mensaje',]
    list_filter = ('de',)
    
    
    
    

admin.site.register(Envios, EnviosAdmin)




