from django.conf.urls import patterns, url
from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView

from models import Propietari, Hort, Arbre
from forms import HortForm, ArbreForm
from views import HortCreate, ArbreCreate, HortDetail, HortList

urlpatterns = patterns('',
    # List latest 5 horts: /myhorts/
    url(r'^$',
        HortList.as_view(),
        name='hort_list'),
        
    # List horts: /myhorts/horts.json
    url(r'^horts\.(?P<extension>(json|xml))$',
        HortList.as_view(),
        name='hort_detail'),

    # Hort details, ex.: /myhorts/horts/1/
    url(r'^horts/(?P<pk>\d+)/$',
        HortDetail.as_view(),
        name='hort_detail'),

    # hort details, ex.: /myhorts/horts/1.json
    url(r'^horts/(?P<pk>\d+)\.(?P<extension>(json|xml))$',
        HortDetail.as_view(),
        name='hort_detail_conneg'),
        
    # Create a Hort: /myhorts/horts/create/
    url(r'^horts/create/$',
        HortCreate.as_view(),
        name='hort_create'),

    # Edit hort details, ex: /myhorts/horts/1/edit/
    url(r'^horts/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model=Hort,
            form_class=HortForm,
            template_name='myhorts/form.html'),
    name='hort_edit'),

    # Hort arbre details, ex: /myhorts/horts/1/arbres/1/
    url(r'^horts/(?P<pkr>\d+)/arbres/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Arbre,
            template_name='myhorts/arbre_detail.html'),
        name='arbre_detail'),

    # Create a restaurant dish, ex: /myhorts/horts/1/arbres/create/
    url(r'^horts/(?P<pk>\d+)/arbres/create/$',
        ArbreCreate.as_view(),
        name='arbre_create'),
        
    # Edit restaurant dish details, ex: /myhorts/horts/1/arbres/1/edit/
    url(r'^horts/(?P<pkr>\d+)/arbres/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model=Arbre,
            form_class=ArbreForm,
            template_name='myhorts/form.html'),
        name='arbre_edit'),
)
