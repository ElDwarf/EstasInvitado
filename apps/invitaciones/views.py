from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.invitaciones.models import Evento, Familia, Galeria, Invitados
from apps.invitaciones.forms import newPaisForm, newProvinciaForm, newLocalidadForm, newDomicilioForm, newFamiliaForm, newInvitadoForm, newEventoForm, viewInvitacionForm


def new_user(request):
    layout = 'vertical'
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
    else:
        form = UserCreationForm()
    return render_to_response('form.html', RequestContext(request, {
        'form': form,
        'layout': layout,
        'title': 'Alta de usuario:',
        }))


def logoutuser(request):
    logout(request)
    return HttpResponseRedirect("/")


@login_required
def write_pais(request):
    layout = 'vertical'

    if request.method == 'POST':
        form = newPaisForm(request.POST)
        if form.is_valid():
            request.session['Pais'] = 'Pais: Argentina'
            new_req = form.save(commit=False)
            new_req.save()
    else:
        form = newPaisForm()
    return render_to_response('form.html', RequestContext(request, {
        'form': form,
        'layout': layout,
        'title': 'Alta de pais:',
        }))


@login_required
def write_provincia(request):
    layout = 'vertical'

    if request.method == 'POST':
        form = newProvinciaForm(request.POST)
        if form.is_valid():
            new_req = form.save(commit=False)
            new_req.save()
    else:
        form = newProvinciaForm()
    return render_to_response('form.html', RequestContext(request, {
        'form': form,
        'layout': layout,
        'title': 'Alta de provincia:',
        }))


@login_required
def write_localidad(request):
    layout = 'vertical'

    if request.method == 'POST':
        form = newLocalidadForm(request.POST)
        if form.is_valid():
            new_req = form.save(commit=False)
            new_req.save()
    else:
        form = newLocalidadForm()
    return render_to_response('form.html', RequestContext(request, {
        'form': form,
        'layout': layout,
        'title': 'Alta de localidad:',
        }))


@login_required
def write_domicilio(request):
    layout = 'vertical'

    if request.method == 'POST':
        form = newDomicilioForm(request.POST)
        if form.is_valid():
            new_req = form.save(commit=False)
            new_req.save()
    else:
        form = newDomicilioForm()
    return render_to_response('form.html', RequestContext(request, {
        'form': form,
        'layout': layout,
        'title': 'Alta de Domicilio:',
        }))


@login_required
def write_familia(request):
    layout = 'vertical'

    if request.method == 'POST':
        form = newFamiliaForm(request.POST)
        if form.is_valid():
            new_req = form.save(commit=False)
            new_req.save()
    else:
        form = newFamiliaForm()
    return render_to_response('form.html', RequestContext(request, {
        'form': form,
        'layout': layout,
        'title': 'Alta de Domicilio:',
        }))


@login_required
def write_invitado(request):
    layout = 'vertical'

    if request.method == 'POST':
        form = newInvitadoForm(request.POST)
        if form.is_valid():
            new_req = form.save(commit=False)
            new_req.save()
    else:
        form = newInvitadoForm()
    return render_to_response('form.html', RequestContext(request, {
        'form': form,
        'layout': layout,
        'title': 'Alta de Domicilio:',
        }))


@login_required
def write_evento(request):
    layout = 'vertical'

    if request.method == 'POST':
        form = newEventoForm(request.POST)
        if form.is_valid():
            new_req = form.save(commit=False)
            new_req.save()
    else:
        form = newEventoForm()
    return render_to_response('form.html', RequestContext(request, {
        'form': form,
        'layout': layout,
        'title': 'Alta de Domicilio:',
        }))


def view_invitacion(request):
    layout = 'vertical'
    if request.method == 'POST':
        form = viewInvitacionForm(request.POST)
        if form.is_valid():
            new_req = form.save(commit=False)
            print new_req
            request.session['nroInvitacion'] = request.POST.get('project', '')
            #new_req.save()
    else:
        form = viewInvitacionForm()
    return render_to_response('formInvitacion.html', RequestContext(request, {
        'form': form,
        'layout': layout,
        }))



def index(request):
    layout = 'vertical'
    if request.method == 'POST':
        form = viewInvitacionForm(request.POST)
        request.session['codInvitacion'] = request.POST.get('codInvitacion', '')
        a = Familia.objects.filter(codInvitacion = request.session['codInvitacion'])
        if len(a) > 0:
            b = Evento.objects.filter(id = a[0].evento.id)
            if len(a[0].evento.nombre) < 1:
                form = viewInvitacionForm()
                print a
            if form.is_valid():
                request.session['codInvitacion'] = request.POST.get('codInvitacion', '')
                a = Familia.objects.filter(codInvitacion = request.session['codInvitacion'])
                b = Evento.objects.filter(id = a[0].evento.id)
                request.session['idEvento'] = a[0].id
                request.session['DescripcionEvento'] = b[0].description
            return render_to_response('evento/index.html', RequestContext(request, {
                'mensaje': 'El proyecto se dio del alta correctamente',
                'form': form,
                'layout': layout,
                }))
        else:
            return render_to_response('index.html', RequestContext(request, {
            'mensaje': 'El proyecto se dio del alta correctamente',
            'alert': True,
            'form': form,
            'layout': layout,
            }))
    else:
        form = viewInvitacionForm()
    return render_to_response('index.html', RequestContext(request, {
        'mensaje': 'El proyecto se dio del alta correctamente',
        'alert': False,
        'form': form,
        'layout': layout,
        }))


def indexevn(request):
    layout = 'vertical'
    if request.method == 'POST':
        form = viewInvitacionForm(request.POST)
        if form.is_valid():
            request.session['codInvitacion'] = request.POST.get('codInvitacion', '')
        return render_to_response('evento/index.html', RequestContext(request, {
            'mensaje': 'El proyecto se dio del alta correctamente',
            'form': form,
            'layout': layout,
            }))

    else:
        form = viewInvitacionForm()
    return render_to_response('evento/index.html', RequestContext(request, {
        'mensaje': 'El proyecto se dio del alta correctamente',
        'form': form,
        'layout': layout,
        }))


def galery(request):
    return render_to_response('evento/galery.html',
        RequestContext(
            request,
            {'galeria': Galeria.objects.filter(evento__id = request.session['idEvento']),}
            ),
                )


def confirmar(request):
    if request.method == 'POST':
        invitados = Invitados.objects.filter(familia__codInvitacion = request.session['codInvitacion'])
        for invitado in invitados:
            if invitado.asiste == 'Si' or invitado.asiste == 'No':
                a = Invitados(id=str(invitado.id),
                            familia = invitado.familia,
                            nombre = invitado.nombre,
                            apellido = invitado.apellido,
                            asiste=invitado.asiste
                            )
            else:
                a = Invitados(id=str(invitado.id),
                    familia = invitado.familia,
                    nombre = invitado.nombre,
                    apellido = invitado.apellido,
                    asiste=str(request.POST.get(str(invitado.id), ''))
                    )
            a.save(force_update=True)
            print str(invitado.id) + str(request.POST.get(str(invitado.id), ''))

    return render_to_response('evento/confirmar.html',
        RequestContext(
            request,
            {'familia': Invitados.objects.filter(familia__codInvitacion = request.session['codInvitacion']),}
            ),
                )


def lugar(request):
    return render_to_response('evento/lugar.html', RequestContext(request, {
        'mensaje': 'El proyecto se dio del alta correctamente',
        }))


def tarjeta(request):
    return render_to_response('evento/tarjeta.html', RequestContext(request, {
        'mensaje': 'El proyecto se dio del alta correctamente',
        }))
