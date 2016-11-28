from django.contrib import admin
from .models import *


class ContactoInline(admin.TabularInline):
    model = Contacto



admin.site.register(Mensaje)




admin.site.register(Bitacora)




admin.site.register(Respuesta)




admin.site.register(Trivia)




admin.site.register(ContactoTipo)




admin.site.register(Envios)




class ContactoAdmin(admin.ModelAdmin):
    list_display = ['contactotipo','nombre','telefono',]
    list_filter = ('contactotipo',)
    search_fields = ['nombre','telefono',]
    
    list_per_page = 100
    

admin.site.register(Contacto, ContactoAdmin)




class PaisAdmin(admin.ModelAdmin):
    list_display = ['nombre','codigo',]
    
    search_fields = ['nombre',]
    
    
    
    inlines = [
    
        ContactoInline,
    
    ]
    

admin.site.register(Pais, PaisAdmin)




