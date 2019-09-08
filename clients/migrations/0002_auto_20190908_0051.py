# Generated by Django 2.1.9 on 2019-09-08 00:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='seancehistorique',
            name='nom',
            field=models.CharField(default='Anonnyme', max_length=255),
        ),
        migrations.AddField(
            model_name='seancehistorique',
            name='versement',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='seancehistorique',
            name='client',
            field=models.ForeignKey(blank='true', null='true', on_delete=django.db.models.deletion.CASCADE, to='clients.Client'),
        ),
    ]