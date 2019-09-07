# Generated by Django 2.1.9 on 2019-09-06 19:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Caisse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('ouverture', models.IntegerField(default=0)),
                ('fermeture', models.IntegerField(null=True)),
                ('fermeture_prevu', models.IntegerField(default=0)),
            ],
        ),
    ]
