# Generated by Django 2.1.7 on 2019-02-27 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GeoPosApp', '0003_auto_20190227_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geoinfo1',
            name='latitude',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='geoinfo1',
            name='longitude',
            field=models.CharField(max_length=50),
        ),
    ]
