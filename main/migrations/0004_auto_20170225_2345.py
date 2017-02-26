# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 14:45
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_dutchorder'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=13, validators=['phone_regex'])),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='dutchorder',
            name='name',
        ),
        migrations.RemoveField(
            model_name='dutchorder',
            name='phone_number',
        ),
        migrations.AlterField(
            model_name='dutchorder',
            name='reserve_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 26, 11, 44, 58, 594876)),
        ),
        migrations.AddField(
            model_name='dutchorder',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.User'),
            preserve_default=False,
        ),
    ]