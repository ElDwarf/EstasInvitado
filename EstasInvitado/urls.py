from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

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
    url(r'^home$', direct_to_template,
                   {'template': 'index.html'}, "home"),
)
