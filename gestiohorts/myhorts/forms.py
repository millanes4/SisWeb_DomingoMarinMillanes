from django.forms import ModelForm
from myhorts.models import Hort, Arbre

class HortForm(ModelForm):
    class Meta:
        model = Hort
        exclude = ('user', 'date',)

class ArbreForm(ModelForm):
    class Meta:
        model = Arbre
        exclude = ('hort', 'user', 'date',)
