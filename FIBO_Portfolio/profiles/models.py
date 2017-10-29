from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
    image = models.FileField(verbose_name = ("Profile Picture"), upload_to ="profiles", max_length = 255, null=True, blank=True)
    bio = models.TextField(max_length = 500, default = True, blank = True)
    birthDate = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=255, default = True, blank=True)
    phone = models.CharField(max_length=63, default = True, blank = True)
    emailConfirmed = models.BooleanField(default=False)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user = instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

class Activity(models.Model):
    name = models.CharField(max_length=250)
    category = models.CharField(max_length=250, blank=True, null=True)
    description = models.CharField(max_length=5000, blank=True, null=True)
    location = models.CharField(max_length=250, blank=True, null=True)
    startDate = models.DateField(blank=True, null=True)
    endDate = models.DateField(blank=True, null=True)
    isVerified = models.BooleanField(default = False)
