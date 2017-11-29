# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-29 05:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import profiles.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('category', models.CharField(blank=True, max_length=250, null=True)),
                ('description', models.CharField(blank=True, max_length=5000, null=True)),
                ('location', models.CharField(blank=True, max_length=250, null=True)),
                ('startDate', models.DateField(blank=True, null=True)),
                ('endDate', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ActivityImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=profiles.models.activity_dir_path)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Activity')),
            ],
        ),
        migrations.CreateModel(
            name='EducationBackground',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=100)),
                ('major', models.CharField(max_length=100)),
                ('school', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(max_length=10)),
                ('creditTotal', models.DecimalField(decimal_places=1, max_digits=3)),
                ('GPA', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ifVerified', models.BooleanField(default=False)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Activity')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(upload_to=profiles.models.user_dir_path, verbose_name='Profile Picture')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('birthDate', models.DateField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=255)),
                ('phone', models.CharField(blank=True, max_length=50)),
                ('emergencyPhone', models.CharField(default='-', max_length=50)),
                ('congenitalDisease', models.CharField(default='None', max_length=50)),
                ('emailConfirmed', models.BooleanField(default=False)),
                ('account_type', models.CharField(choices=[('ST', 'Student'), ('LE', 'Lecturer'), ('SF', 'Staff')], default='Student', max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('admission', models.CharField(blank=True, max_length=100)),
                ('scholarship', models.CharField(default='None', max_length=100)),
                ('friendViewPersonalInfo', models.BooleanField(default=False)),
                ('publicViewPersonalInfo', models.BooleanField(default=False)),
                ('friendViewAcademicInfo', models.BooleanField(default=False)),
                ('publicViewAcademicInfo', models.BooleanField(default=False)),
                ('friendViewExpInfo', models.BooleanField(default=False)),
                ('publicViewExpInfo', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to=profiles.models.user_dir_path)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='participation',
            name='participant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Profile'),
        ),
        migrations.AddField(
            model_name='grade',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Profile'),
        ),
        migrations.AddField(
            model_name='educationbackground',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Profile'),
        ),
        migrations.AddField(
            model_name='activity',
            name='participants',
            field=models.ManyToManyField(related_name='participant', through='profiles.Participation', to='profiles.Profile'),
        ),
        migrations.AddField(
            model_name='activity',
            name='supervisors',
            field=models.ManyToManyField(related_name='supervisor', to='profiles.Profile'),
        ),
        migrations.AddField(
            model_name='ability',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Profile'),
        ),
    ]
