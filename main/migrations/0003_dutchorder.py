# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 10:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_image_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='DutchOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(blank=True, max_length=13, validators=['phone_regex'])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('reserve_at', models.DateTimeField()),
                ('quantity', models.PositiveSmallIntegerField()),
                ('total_charge', models.PositiveIntegerField()),
            ],
        ),
    ]
