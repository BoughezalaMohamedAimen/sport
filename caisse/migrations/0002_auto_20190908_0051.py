# Generated by Django 2.1.9 on 2019-09-08 00:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caisse', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caisse',
            name='date',
            field=models.DateField(blank='true', default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='caisse',
            name='fermeture',
            field=models.IntegerField(blank='true', null=True),
        ),
        migrations.AlterField(
            model_name='caisse',
            name='fermeture_prevu',
            field=models.IntegerField(blank='true', default=0),
        ),
        migrations.AlterField(
            model_name='caisse',
            name='ouverture',
            field=models.IntegerField(blank='true', default=0),
        ),
    ]
