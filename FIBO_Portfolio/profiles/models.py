from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
    avatar = models.FileField(verbose_name = ("Profile Picture"), upload_to ="profiles", max_length = 255)
    bio = models.TextField(max_length = 500)
    birthDate = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    emergencyPhone = models.CharField(max_length=50)
    congenitalDisease = models.CharField(max_length = 50, default="none")
    emailConfirmed = models.BooleanField(default=False)
    position = models.CharField(max_length = 100)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user = instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.user.save()

class Ability(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)

class Grade(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    semester = models.CharField(max_length = 10)
    creditTotal = models.DecimalField(max_digits=3, decimal_places=1)
    GPA = models.DecimalField(max_digits=3, decimal_places=2)

class EducationBackground(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    degree = models.CharField(max_length = 100)
    major = models.CharField(max_length = 100)
    school = models.CharField(max_length = 100)

def user_dir_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class UserImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.FileField(upload_to=user_dir_path)
