from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    # url(r'^$', 'IntentoTreiky.views.home', name='home'),
    # url(r'^IntentoTreiky/', include('IntentoTreiky.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # MediaURL
     url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
         'document_root': settings.MEDIA_ROOT,
         }),


    # Mi URL:
    url(r'^$', direct_to_template,
                   {'template': 'index.html'}, "home"),
    url(r'^accounts/profile/$', direct_to_template,
                   {'template': 'index.html'}, "home"),
    url(r'^home$',
        'apps.invitaciones.views.index', name='home'),
    url(r'^logout/$',
        'apps.invitaciones.views.logoutuser', name='logoutuser'),
    url(r'^write_pais/$',
        'apps.invitaciones.views.write_pais', name='write_pais'),
    url(r'^write_provincia/$',
        'apps.invitaciones.views.write_provincia', name='write_provincia'),
    url(r'^write_localidad/$',
        'apps.invitaciones.views.write_localidad', name='write_localidad'),
    url(r'^write_domicilio/$',
        'apps.invitaciones.views.write_domicilio', name='write_domicilio'),
    url(r'^write_familia/$',
        'apps.invitaciones.views.write_familia', name='write_familia'),
    url(r'^write_invitado/$',
        'apps.invitaciones.views.write_invitado', name='write_invitado'),
    url(r'^write_evento/$',
        'apps.invitaciones.views.write_evento', name='write_evento'),
    url(r'^write_evento/$',
        'apps.invitaciones.views.write_evento', name='write_evento'),
    url(r'^view_invitacion/$',
        'apps.invitaciones.views.view_invitacion', name='view_invitacion'),
    url(r'^new_user/$',
        'apps.invitaciones.views.new_user', name='new_user'),
    url(r'^galery/$',
        'apps.invitaciones.views.galery', name='galery'),
)
