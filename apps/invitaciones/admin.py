# -*- coding: utf-8 *-*
from django.contrib import admin
from apps.invitaciones.models import Pais, Provincia, Localidad, Domicilio, Evento, Familia, Invitados, Galeria, RelaInvitFlia


class provinciaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais',)
    search_fields = ('nombre', 'pais__nombre',)


class localidadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'provincia',)
    search_fields = ('nombre', 'provincia__nombre', 'provincia__pais__nombre',)


class domicilioAdmin(admin.ModelAdmin):
    list_display = ('calle', 'numeracion', 'piso', 'departamento', 'localidad',)
    search_fields = ('calle', 'numeracion', 'piso', 'departamento', 'localidad__nombre', 'localidad__provincia__nombre',)


class eventoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fechaevento', 'description',)
    search_fields = ('nombre', 'fechaevento', 'description',)


class familiaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codInvitacion', 'evento', 'confirmado',)
    search_fields = ('nombre', 'codInvitacion', 'evento', 'confirmado',)


class invitadosAdmin(admin.ModelAdmin):
    list_display = ('familia', 'apellido', 'nombre', 'asiste',)
    search_fields = ('familia__nombre', 'apellido', 'nombre', 'asiste',)


class InfFliaAdmin(admin.ModelAdmin):
    list_display = ('familia', 'invitacion',)
    search_fields = ('familia', 'invitacion',)


admin.site.register(Pais,)
admin.site.register(Provincia, provinciaAdmin)
admin.site.register(Localidad, localidadAdmin)
admin.site.register(Domicilio, domicilioAdmin)
admin.site.register(Evento, eventoAdmin)
admin.site.register(Familia, familiaAdmin)
admin.site.register(Invitados, invitadosAdmin)
admin.site.register(Galeria)
admin.site.register(RelaInvitFlia, InfFliaAdmin)
