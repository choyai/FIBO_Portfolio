# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-29 10:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, max_length=255, null=True, upload_to='profiles', verbose_name='Profile Picture')),
                ('bio', models.TextField(blank=True, default=True, max_length=500)),
                ('birthDate', models.DateField(blank=True, null=True)),
                ('location', models.CharField(blank=True, default=True, max_length=255)),
                ('phone', models.CharField(blank=True, default=True, max_length=63)),
                ('emailConfirmed', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
