# Generated by Django 2.1.9 on 2019-09-06 19:08

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('caisse', '0001_initial'),
        ('forfaits', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Abonnement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_heure', models.DateTimeField(blank='true', default=datetime.datetime.now)),
                ('date_debut', models.DateField(default=datetime.datetime.now)),
                ('nbr_mois', models.IntegerField(default=1)),
                ('montant', models.IntegerField(blank='true')),
                ('remise', models.IntegerField(default=0)),
                ('versement', models.IntegerField(default=0)),
                ('caisse', models.ForeignKey(blank='true', on_delete=django.db.models.deletion.CASCADE, to='caisse.Caisse')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rfid', models.CharField(max_length=255, unique='true')),
                ('sex', models.CharField(choices=[('Homme', 'Homme'), ('Femme', 'Femme')], max_length=25)),
                ('nom', models.CharField(max_length=255)),
                ('prenom', models.CharField(max_length=255)),
                ('date_naissance', models.DateField()),
                ('photo', models.ImageField(blank='true', null='true', upload_to='clients')),
                ('telephone', models.CharField(blank=True, max_length=10, null='true')),
                ('telephone_urgence', models.CharField(blank=True, max_length=10, null='true')),
                ('adresse', models.CharField(blank=True, max_length=255, null='true')),
                ('email', models.EmailField(blank=True, max_length=70, null='true')),
                ('seance', models.IntegerField(default=0)),
                ('date_debut', models.DateField(blank='true', default=datetime.datetime.now)),
                ('date_fin', models.DateField(blank='true', default=datetime.datetime.now)),
                ('credit', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='SeanceHistorique',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_heure', models.DateTimeField(blank='true', default=datetime.datetime.now)),
                ('client', models.ForeignKey(blank='true', on_delete=django.db.models.deletion.CASCADE, to='clients.Client')),
            ],
        ),
        migrations.AddField(
            model_name='abonnement',
            name='client',
            field=models.ForeignKey(blank='true', on_delete=django.db.models.deletion.CASCADE, to='clients.Client'),
        ),
        migrations.AddField(
            model_name='abonnement',
            name='forfait',
            field=models.ForeignKey(blank='true', on_delete=django.db.models.deletion.CASCADE, to='forfaits.Forfait'),
        ),
    ]
