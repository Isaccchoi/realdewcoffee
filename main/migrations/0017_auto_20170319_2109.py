# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-19 12:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20170313_2003'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dutchorder',
            options={'ordering': ['-created_at', '-id']},
        ),
    ]
