# -*- coding: utf-8 *-*
from django.forms import ModelForm, Textarea, Select, TextInput, DateTimeInput
from django import forms
from apps.invitaciones.models import Pais, Provincia, Localidad, Domicilio, Evento, Familia, Invitados
from django.contrib.auth.models import User


class newPaisForm(ModelForm):

    #def __init__(self, *args, **kwargs):
    #    super(newUserForm, self).__init__(*args, **kwargs)
    #    self.fields['username'].label = "Nombre de usuario"
    #    self.fields['first_name'].label = "Nombre"
    #    self.fields['last_name'].label = "Apellido"
    #    self.fields['username'].error_messages = {
    #        'required': 'El nombre de usuario es requerido'}
    #    self.fields['last_name'].error_messages = {
    #        'required': 'La nombre es requerida'}
    #    self.fields['last_name'].error_messages = {
    #        'required': 'El apellido es requerido'}
    #    self.fields['email'].error_messages = {
    #        'required': 'El Email es requerido'}

    class Meta:
        model = Pais
        widgets = {
            'nombre': TextInput,
        }
        fields = ('nombre',)


class newProvinciaForm(ModelForm):

    class Meta:
        model = Provincia
        widgets = {
            'nombre': TextInput(),
            'pais': Select(),
        }
        fields = ('nombre', 'pais')


class newLocalidadForm(ModelForm):

    class Meta:
        model = Localidad
        widgets = {
            'nombre': TextInput(),
            'provincia': Select(),
        }
        fields = ('nombre', 'provincia')


class newDomicilioForm(ModelForm):

    class Meta:
        model = Domicilio
        widgets = {
            'nombre': TextInput(),
            'calle': TextInput(),
            'numeracion': TextInput(),
            'piso': TextInput(),
            'departamento': TextInput(),
            'CodPostal': TextInput(),
            'localidad': Select(),
        }
        fields = ('nombre', 'calle', 'numeracion', 'piso', 'departamento', 'CodPostal','localidad')


class newFamiliaForm(ModelForm):

    class Meta:
        model = Familia
        widgets = {
            'evento': Select(),
            'nombre': TextInput(),
            'description': TextInput(),
            'codInvitacion': TextInput(),
            'domicilio': Select(),
            'email': TextInput(),
            'telefono': TextInput(),
        }
        fields = ('evento', 'nombre', 'description', 'codInvitacion', 'domicilio', 'email', 'telefono')


class newInvitadoForm(ModelForm):

    class Meta:
        model = Invitados
        widgets = {
            'familia': Select(),
            'nombre': TextInput(),
            'apellido': TextInput(),
        }
        fields = ('familia', 'nombre', 'apellido')


class newEventoForm(ModelForm):

    class Meta:
        model = Evento
        widgets = {
            'nombre': TextInput(),
            'fechaevento': DateTimeInput(),
            'domicilio': Select(),
        }
        fields = ('nombre', 'domicilio', 'fechaevento', 'description', 'mensajeinvitacion')


class viewFamiliaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(viewFamiliaForm, self).__init__(*args, **kwargs)
        self.fields['codInvitacion'].label = "Ingrese el codigo de su invitacion"

    class Meta:
        model = Familia
        widgets = {
            'codInvitacion': TextInput(),
        }
        fields = ('codInvitacion',)
