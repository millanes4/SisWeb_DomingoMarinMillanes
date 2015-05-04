from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

#from myhorts.views import *
urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'myhorts.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^myhorts/', include('myhorts.urls', namespace='myhorts')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
    url(r'^accounts/profile/$', include('myhorts.urls', namespace='myhorts')),


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
