# Generated by Django 2.0.13 on 2019-10-03 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='CIN',
            field=models.CharField(default=True, max_length=10),
        ),
        migrations.AddField(
            model_name='patient',
            name='profession',
            field=models.CharField(default=True, max_length=100),
        ),
    ]
