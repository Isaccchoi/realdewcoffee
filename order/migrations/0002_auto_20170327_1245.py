# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-27 03:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beverage',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
