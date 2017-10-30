from django.db import models
from django.contrib.auth.models import User, Permission, Group
from profiles.models import Profile

class Activity(models.Model):
    participants = models.ManyToManyField(
        Profile,
        through='Participation',
        )
    name = models.CharField(max_length=250)
    category = models.CharField(max_length=250, blank=True, null=True)
    description = models.CharField(max_length=5000, blank=True, null=True)
    location = models.CharField(max_length=250, blank=True, null=True)
    startDate = models.DateField(blank=True, null=True)
    endDate = models.DateField(blank=True, null=True)

class Participation(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    ifVerified = models.BooleanField(default = False)
