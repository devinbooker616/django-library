# Generated by Django 2.2.5 on 2019-11-08 19:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='published',
            field=models.DateField(verbose_name=datetime.datetime(2019, 11, 8, 19, 17, 19, 519233)),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='datetime',
            field=models.DateField(verbose_name=datetime.datetime(2019, 11, 8, 19, 17, 19, 520353)),
        ),
    ]
