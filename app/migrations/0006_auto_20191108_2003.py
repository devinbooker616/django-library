# Generated by Django 2.2.5 on 2019-11-08 20:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20191108_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='published',
            field=models.DateField(verbose_name=datetime.datetime(2019, 11, 8, 20, 3, 28, 411760)),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='datetime',
            field=models.DateField(verbose_name=datetime.datetime(2019, 11, 8, 20, 3, 28, 413050)),
        ),
    ]
