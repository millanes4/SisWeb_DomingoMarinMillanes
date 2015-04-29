from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from myhorts.views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gestiohorts.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^myhorts/',  include('myhorts.urls',  namespace='myhorts')),
    url(r'^admin/', include(admin.site.urls)),
)
