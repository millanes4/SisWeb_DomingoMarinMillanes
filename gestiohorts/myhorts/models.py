# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date


class Hort(models.Model):
    nom = models.TextField(default="")
    provincia = models.TextField(default="", null=False)
    municipi = models.TextField(default="", null=False)
    poligon = models.IntegerField(null=False)
    parcela = models.IntegerField(null=False)
    recinte = models.IntegerField(null=False)
    date = models.DateField(default=date.today)

    def __unicode__(self):
        return u"%s" % self.nom

    def get_absolute_url(self):
        return reverse('myhorts:hort_detail', kwargs={'pk': self.pk})


class Propietari(models.Model):
    user = models.ForeignKey(User, default=1)
    nom = models.TextField(null=False)
    cognoms = models.TextField(null=False)
    dni = models.TextField(null=False)
    email = models.EmailField(null=False)

    def __unicode__(self):
        return u"%s" % self.nom

    def get_absolute_url(self):
        return reverse('myhorts:propietari_detail', kwargs={'pkr': self.hort.pk, 'pk': self.pk})


class Arbre(models.Model):
    tipus = models.TextField(null=False)
    varietat = models.TextField(blank=True, null=False)
    data_recolecta = models.DateField(default=date.today,null=False)
    data_planta = models.DateField(default=date.today,null=False)
    
    def __unicode__(self):
        return u"%s" % self.tipus


class Arbre_Hort(models.Model):
    idhort = models.ForeignKey(Hort, null=False)
    idarbre = models.ForeignKey(Arbre, null=False)
    cantitat = models.IntegerField(null=False)

