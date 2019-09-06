from django.db import models
from datetime import datetime
# Create your models here.
class Caisse(models.Model):
    date=models.DateField(default=datetime.now)


class Transaction(models.Model):
    caisse=model.ForeignKey(Caisse,on_delete=models.CASCADE,blank='true')
    montant=model.IntegerField()
    type=model.CharField(max_length=225,choices=(('Abonnement','Abonement'),('Vérsement','Vérsement')))
    client=model.ForeignKey(Client,on_delete=models.CASCADE,blank='true',null='true')
