from django.conf.urls import patterns, include, url
import stackoverflow.views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'stackoverflow',stackoverflow.views.hello_world),
    #url(r'^$', 'skillstack.views.home', name='home'),
    #url(r'^skillstack/', include('skillstack.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
