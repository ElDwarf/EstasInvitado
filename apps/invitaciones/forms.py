# -*- coding: utf-8 *-*
from django.forms import ModelForm, Select, TextInput, DateTimeInput, Textarea
from apps.invitaciones.models import Pais, Provincia, Localidad, Domicilio, Evento, Familia, Invitados, Galeria


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
            'calle': TextInput(),
            'numeracion': TextInput(),
            'piso': TextInput(),
            'departamento': TextInput(),
            'CodPostal': TextInput(),
            'localidad': Select(),
        }
        fields = ('calle', 'numeracion', 'piso', 'departamento', 'CodPostal','localidad')


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
        fields = ('nombre', 'domicilio', 'fechaevento', 'description')


class newPictureForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(newPictureForm, self).__init__(*args, **kwargs)
        self.fields['evento'].label = "Seleccione el Evento"
        self.fields['orden'].label = "Ingrese la posicion (solo numeros)"
        self.fields['nombre'].label = "Ingrese el nombre de la foto"
        self.fields['descripcion'].label = "Ingrese la descripcion de la foto"
        self.fields['urlfoto'].label = "Ingrese la URL de la foto"
        self.fields['evento'].error_messages = {
            'required': 'Debe seleccionar un evento'}
        self.fields['orden'].error_messages = {
            'required': 'El campo es requerido'}
        self.fields['nombre'].error_messages = {
            'required': 'El campo es requerido'}
        self.fields['descripcion'].error_messages = {
            'required': 'El campo es requerido'}
        self.fields['urlfoto'].error_messages = {
            'required': 'El campo es requerido'}

    class Meta:
        model = Galeria
        widgets = {
            'evento': Select(),
            'orden': TextInput(),
            'nombre': TextInput(),
            'descripcion': Textarea(),
            'urlfoto': TextInput(),
        }
        fields = ('evento', 'orden', 'nombre', 'descripcion', 'urlfoto',)


class viewInvitacionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(viewInvitacionForm, self).__init__(*args, **kwargs)
        self.fields['codInvitacion'].label = "Código de invitación"

    class Meta:
        model = Familia
        widgets = {
            'codInvitacion': TextInput(),
        }
        fields = ('codInvitacion',)

