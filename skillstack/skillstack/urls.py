from django.conf.urls import patterns, include, url
<<<<<<< HEAD
from django.conf import settings
=======
import stackoverflow.views
>>>>>>> 4f3d6aa72af3926fcf19f8b0bdd593771509b6ca

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    r'^static/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': 'static'}
    # Examples:
    url(r'stackoverflow',stackoverflow.views.hello_world),
    url(r'tests',stackoverflow.views.test_stackoverflow),
    #url(r'^$', 'skillstack.views.home', name='home'),
    #url(r'^skillstack/', include('skillstack.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
