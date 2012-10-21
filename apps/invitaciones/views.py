from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
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
    layout = 'vertical'
    logout(request)
    if request.method == 'POST':
        form = viewInvitacionForm(request.POST)
        if form.is_valid():
            request.session['codInvitacion'] = request.POST.get('codInvitacion', '')
            print request.session['codInvitacion']
    else:
        form = viewInvitacionForm()
    return render_to_response('index.html', RequestContext(request, {
        'mensaje': 'El proyecto se dio del alta correctamente',
        'form': form,
        'layout': layout,
        }))


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


def galery(request):
    return render_to_response('galery.html', RequestContext(request, {
        'mensaje': 'El proyecto se dio del alta correctamente',
        }))


def index(request):
    layout = 'vertical'

    if request.method == 'POST':
        form = viewInvitacionForm(request.POST)
        if form.is_valid():
            request.session['codInvitacion'] = request.POST.get('codInvitacion', '')
            print request.session['codInvitacion']
    else:
        form = viewInvitacionForm()
    return render_to_response('index.html', RequestContext(request, {
        'mensaje': 'El proyecto se dio del alta correctamente',
        'form': form,
        'layout': layout,
        }))
