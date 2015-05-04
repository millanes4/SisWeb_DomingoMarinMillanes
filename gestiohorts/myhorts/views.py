from django.shortcuts import render

# Create your views here.

from django.core import serializers

from django.utils import timezone

from django.core import urlresolvers
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.edit import CreateView

from models import Arbre, Propietari, Hort
from forms import HortForm, ArbreForm
from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):
    return render_to_response('myhorts/mainpage.html', context_instance=RequestContext(request))

class ConnegResponseMixin(TemplateResponseMixin):
    def render_json_object_response(self, objects, **kwargs):
        json_data = serializers.serialize(u"json", objects, **kwargs)
        return HttpResponse(json_data, content_type=u"application/json")

    def render_xml_object_response(self, objects, **kwargs):
        xml_data = serializers.serialize(u"xml", objects, **kwargs)
        return HttpResponse(xml_data, content_type=u"application/xml")

    def render_to_response(self, context, **kwargs):
        if 'extension' in self.kwargs:
            try:
                objects = [self.object]
            except AttributeError:
                objects = self.object_list
            if self.kwargs['extension'] == 'json':
                return self.render_json_object_response(objects=objects)
            elif self.kwargs['extension'] == 'xml':
                return self.render_xml_object_response(objects=objects)
        else:
            return super(ConnegResponseMixin, self).render_to_response(context)


class HortDetail(DetailView):
    model = Hort
    template_name = 'myhorts/hort_detail.html'

    def get_context_data(self, **kwargs):
        context = super(HortDetail, self).get_context_data(**kwargs)
        return context


class HortList(ListView, ConnegResponseMixin):
    model = Hort
    queryset = Hort.objects.filter(date__lte=timezone.now()).order_by('date')[:5]
    context_object_name = 'latest_hort_list'
    template_name = 'myhorts/hort_list.html'


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
        
def submit(request):
    # global alphabet_array

    if request.method == "POST":
        print request.POST['hort']

    return render(request, 'index.html', {})


	#output = template.render(variables)
	#return HttpResponse(output)
