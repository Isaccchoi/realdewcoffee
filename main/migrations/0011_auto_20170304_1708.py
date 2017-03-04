# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-04 08:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20170302_2256'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryForImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterModelOptions(
            name='dutchorder',
            options={'ordering': ['created_at', '-id']},
        ),
        migrations.AddField(
            model_name='image',
            name='categotyimage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.CategoryForImage'),
        ),
    ]
