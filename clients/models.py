from django.db import models
import datetime
from dateutil.relativedelta import relativedelta

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
    seance=models.PositiveIntegerField(default=0)
    date_debut=models.DateField(default=datetime.datetime.now,blank='true')
    date_fin=models.DateField(default=datetime.datetime.now,blank='true')
    credit=models.PositiveIntegerField(default=0)

    # def renouvler(self,forfait,mois):
    #     self.seance+=forfait.nbr_seance*mois
    #     self.date_debut=datetime.date.today()
    #     self.date_fin=datetime.date.today()+ relativedelta(months=mois)
