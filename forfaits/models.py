from django.db import models

# Create your models here.
class Forfait(models.Model):
    nom=models.CharField(max_length=255)
    nbr_seance=models.PositiveIntegerField()
    prix=models.PositiveIntegerField()
