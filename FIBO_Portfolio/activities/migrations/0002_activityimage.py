# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-30 13:02
from __future__ import unicode_literals

import activities.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to=activities.models.activity_dir_path)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activities.Activity')),
            ],
        ),
    ]
