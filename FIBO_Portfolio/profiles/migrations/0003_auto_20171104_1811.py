# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-04 11:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20171031_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='emergencyPhone',
            field=models.CharField(default='-', max_length=50),
        ),
    ]