from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
    avatar = models.FileField(verbose_name = ("Profile Picture"), upload_to ="profiles", max_length = 255)
    bio = models.TextField(max_length = 500, blank=True)
    birthDate = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    emergencyPhone = models.CharField(max_length=50, default = "-")
    congenitalDisease = models.CharField(max_length = 50, default="None")
    emailConfirmed = models.BooleanField(default=False)
    position = models.CharField(max_length = 100)
    admission = models.CharField(max_length = 100)
    scholarship = models.CharField(max_length = 100, default = "None")
    friendViewPersonalInfo = models.BooleanField(default = False)
    publicViewPersonalInfo = models.BooleanField(default = False)
    friendViewAcademicInfo = models.BooleanField(default = False)
    publicViewAcademicInfo = models.BooleanField(default = False)
    friendViewExpInfo = models.BooleanField(default = False)
    publicViewExpInfo = models.BooleanField(default = False)


    def get_absolute_url(self):
        return reverse('profiles:profile', kwargs={'pk': self.pk})

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

class Activity(models.Model):
    participants = models.ManyToManyField(
        User,
        through='Participation',
        related_name='participant',
        )
    supervisors = models.ManyToManyField(
        User,
        through='Supervision',
        related_name='supervisor',
    )

    name = models.CharField(max_length=250)
    category = models.CharField(max_length=250, blank=True, null=True)
    description = models.CharField(max_length=5000, blank=True, null=True)
    location = models.CharField(max_length=250, blank=True, null=True)
    startDate = models.DateField(blank=True, null=True)
    endDate = models.DateField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('activities:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

class Supervision(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    supervisor = models.ForeignKey(User, on_delete=models.CASCADE)

class Participation(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    participant = models.ForeignKey(User, on_delete=models.CASCADE)
    ifVerified = models.BooleanField(default = False)

def activity_dir_path(instance, filename):
    return 'activity_{0}/{1}'.format(instance, filename)

class ActivityImage(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = activity_dir_path)
