from django.db import models

class Activity(models.Model):
    name = models.CharField(max_length=250)
