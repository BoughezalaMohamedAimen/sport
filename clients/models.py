from django.db import models
import datetime
from dateutil.relativedelta import relativedelta
from caisse.models import Caisse
from forfaits.models import Forfait
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Client(models.Model):
    rfid=models.CharField(max_length=255,unique='true')
    sex=models.CharField(max_length=25,choices=(('Homme','Homme'),('Femme','Femme')))
    nom=models.CharField(max_length=255)
    prenom=models.CharField(max_length=255)
    date_naissance=models.DateField()
    photo=models.ImageField(upload_to='clients',blank='true',null='true')
    telephone=models.CharField(max_length=10,null='true',blank=True)
    telephone_urgence=models.CharField(max_length=10,null='true',blank=True)
    adresse=models.CharField(max_length=255,null='true',blank=True)
    email = models.EmailField(max_length=70,null='true',blank=True)
    seance=models.IntegerField(default=0)
    date_debut=models.DateField(default=datetime.datetime.now,blank='true')
    date_fin=models.DateField(default=datetime.datetime.now,blank='true')
    credit=models.PositiveIntegerField(default=0)


    def consome(self):
        self.seance-=1
        SeanceHistorique(client=self).save()
        self.save()

    def __str__(self):
        return self.nom+' '+self.prenom


    def renouvler(self,date_debut,forfait,mois,total,versement):
        self.seance+=forfait.nbr_seance*mois
        self.date_debut=date_debut
        self.date_fin=date_debut+ relativedelta(months=mois)
        self.credit+=total-versement
        self.save()



class SeanceHistorique(models.Model):
    date_heure=models.DateTimeField(default=datetime.datetime.now, blank='true')
    client=models.ForeignKey(Client,on_delete=models.CASCADE,blank='true')




class Abonnement(models.Model):
    caisse=models.ForeignKey(Caisse,on_delete=models.CASCADE,blank='true')
    date_heure=models.DateTimeField(default=datetime.datetime.now,blank='true')
    forfait=models.ForeignKey(Forfait,on_delete=models.CASCADE,blank='true')
    date_debut=models.DateField(default=datetime.datetime.now)
    nbr_mois=models.IntegerField(default=1)
    montant=models.IntegerField(blank='true')
    remise=models.IntegerField(default=0)
    versement=models.IntegerField(default=0)
    client=models.ForeignKey(Client,on_delete=models.CASCADE,blank='true')


from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Abonnement)
def my_handler(sender, **kwargs):
    caisse=Caisse.objects.get(date=datetime.date.today())
    caisse.fermeture_prevu+=kwargs['instance'].versement
    caisse.save()
