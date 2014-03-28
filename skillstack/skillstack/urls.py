from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    r'^static/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': 'static'}
    # Examples:
    # url(r'^$', 'skillstack.views.home', name='home'),
    # url(r'^skillstack/', include('skillstack.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
