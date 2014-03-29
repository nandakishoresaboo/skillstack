from django.conf.urls import patterns, include, url
from django.conf import settings
import stackoverflow.views
import skillstack_app.views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static'}),
    url(r'stackoverflow',stackoverflow.views.hello_world),
    url(r'tests',stackoverflow.views.test_stackoverflow),
    url(r'dashboard',skillstack_app.views.dashboard),
    url(r'profile',skillstack_app.views.profile),
    url(r'login',skillstack_app.views.login),
    #url(r'^$', 'skillstack.views.home', name='home'),
    #url(r'^skillstack/', include('skillstack.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
