# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-09-27 01:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='userPasswd',
            field=models.CharField(max_length=255),
        ),
    ]
