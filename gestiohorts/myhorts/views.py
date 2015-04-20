from django.shortcuts import render

# Create your views here.

from django.core import urlresolvers
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.views.generic.edit import CreateView

from models import Arbre, Propietari, Hort
from forms import HortForm, ArbreForm

class HortDetail(DetailView):
    model = Hort
    template_name = 'myhorts/hort_detail.html'

    def get_context_data(self, **kwargs):
        context = super(HortDetail, self).get_context_data(**kwargs)
        return context

class HortCreate(CreateView):
    model = Hort
    template_name = 'myhorts/form.html'
    form_class = HortForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(HortCreate, self).form_valid(form)

class ArbreCreate(CreateView):
    model = Arbre
    template_name = 'myhorts/form.html'
    form_class = ArbreForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.hort = Hort.objects.get(id=self.kwargs['pk'])
        return super(ArbreCreate, self).form_valid(form)

