# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-21 11:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20170319_2109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dutchorder',
            name='user',
        ),
        migrations.DeleteModel(
            name='DutchOrder',
        ),
    ]