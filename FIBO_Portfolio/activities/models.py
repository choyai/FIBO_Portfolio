from django.db import models
import profiles
class Activity(models.Model):
    name = models.CharField(max_length=250)
    category = models.CharField(max_length=250, blank=True, null=True)
    description = models.CharField(max_length=5000, blank=True, null=True)
    location = models.CharField(max_length=250, blank=True, null=True)
    startDate = models.DateField(blank=True, null=True)
    endDate = models.DateField(blank=True, null=True)
    isVerified = models.BooleanField(default = False)

class Image(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    image = models.FileField(blank=True, null=True)
