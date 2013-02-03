from django.db import models
from django.contrib.auth.models import User
import datetime


class Pais(models.Model):
    nombre = models.TextField(max_length=50)

    def __unicode__(self):
        return "%s" % (self.nombre)


class Provincia(models.Model):
    nombre = models.TextField(max_length=50)
    pais = models.ForeignKey(Pais)

    def __unicode__(self):
        return "%s, %s" % (self.nombre, self.pais.nombre)


class Localidad(models.Model):
    nombre = models.TextField(max_length=50)
    provincia = models.ForeignKey(Provincia)

    def __unicode__(self):
        return "%s, %s, %s" % (self.nombre, self.provincia.nombre, self.provincia.pais.nombre)


class Domicilio(models.Model):
    calle = models.TextField(max_length=150)
    numeracion = models.TextField(max_length=5)
    piso = models.TextField(max_length=6)
    departamento = models.TextField(max_length=5)
    CodPostal = models.TextField(max_length=10)
    localidad = models.ForeignKey(Localidad)

    def __unicode__(self):
        return "%s, %s, %s, %s, %s" % (self.calle, self.numeracion, self.piso, self.departamento, self.localidad.nombre)

class Evento(models.Model):

    nombre = models.TextField(max_length=20)
    fechaevento = models.DateTimeField()
    domicilio = models.ForeignKey(Domicilio)
    description = models.TextField(max_length=200)
    fechacreacion = models.DateTimeField(default=datetime.datetime.now)
    autor = models.ForeignKey(User, blank=True, null=True)

    def __unicode__(self):
        return "%s" % (self.nombre)


class Familia(models.Model):
    """
    Model to represent the requerimiento.
    """
    evento = models.ForeignKey(Evento)
    nombre = models.TextField(max_length=30)
    description = models.TextField(max_length=140)
    date_created = models.DateTimeField(default=datetime.datetime.now)
    codInvitacion = models.TextField(max_length=10)
    domicilio = models.ForeignKey(Domicilio)
    email = models.TextField(max_length=150)
    telefono = models.TextField(max_length=150)
    ingresaron = models.TextField(max_length=2, default='N')
    autor = models.ForeignKey(User, blank=True, null=True)

    def __unicode__(self):
        return "Familia: %s" % (
            self.nombre,)


class Invitados(models.Model):
    """
    Model to represent the requerimiento.
    """
    familia = models.ForeignKey(Familia)
    nombre = models.TextField(max_length=10)
    apellido = models.TextField(max_length=10)
    asiste = models.TextField(max_length=2)
    autor = models.ForeignKey(User, blank=True, null=True)

    def __unicode__(self):
        return "%s, %s - Fam: %s" % (
            self.apellido, self.nombre, self.familia.nombre)


class Galeria(models.Model):
    evento = models.ForeignKey(Evento)
    orden = models.TextField(max_length=2)
    nombre = models.TextField(max_length=10)
    descripcion = models.TextField(max_length=200)
    urlfoto = models.TextField()

    def __unicode__(self):
        return "%s" %(self.nombre)


class Invitacion(models.Model):
    evento = models.ForeignKey(Evento)
    mensaje1 = models.TextField(max_length=300)
    mensaje2 = models.TextField(max_length=300)
    mensaje3 = models.TextField(max_length=300)
    cuenta = models.TextField(max_length=20)


class RelaInvitFlia(models.Model):
    familia = models.ForeignKey(Familia)
    invitacion = models.ForeignKey(Invitacion)
