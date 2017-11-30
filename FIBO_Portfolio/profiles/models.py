from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver

def user_dir_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Profile(models.Model):
    student = 'ST'
    lecturer = 'LE'
    staff = 'SF'
    ACCOUNT_TYPES = ((student, 'Student'), (lecturer, 'Lecturer'), (staff, 'Staff'))

    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
    avatar = models.ImageField(verbose_name = ("Profile Picture"), upload_to =user_dir_path)
    bio = models.TextField(max_length = 500, blank=True)
    birthDate = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    emergencyPhone = models.CharField(max_length=50, default = "-")
    congenitalDisease = models.CharField(max_length = 50, default="None")
    emailConfirmed = models.BooleanField(default=False)
    account_type = models.CharField(max_length = 100, choices = ACCOUNT_TYPES, default='Student')
    position = models.CharField(max_length = 100)
    admission = models.CharField(max_length = 100, blank=True)
    scholarship = models.CharField(max_length = 100, default = "None")
    friendViewPersonalInfo = models.BooleanField(default = False)
    publicViewPersonalInfo = models.BooleanField(default = False)
    friendViewAcademicInfo = models.BooleanField(default = False)
    publicViewAcademicInfo = models.BooleanField(default = False)
    friendViewExpInfo = models.BooleanField(default = False)
    publicViewExpInfo = models.BooleanField(default = False)


    def __str__(self):
        return self.user.first_name

    def is_staff(self):
        return self.account_type in (self.staff, self.lecturer)

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

    def __str__(self):
        return self.profile.user.first_name + self.name

class Grade(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    semester = models.CharField(max_length = 10)
    creditTotal = models.DecimalField(max_digits=3, decimal_places=1)
    GPA = models.DecimalField(max_digits=3, decimal_places=2)
    def get_absolute_url(self):
            return reverse('profiles:academic', kwargs={'pk': self.pk})

class EducationBackground(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    degree = models.CharField(max_length = 100)
    major = models.CharField(max_length = 100)
    school = models.CharField(max_length = 100)


class UserImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.FileField(upload_to=user_dir_path)

    def __str__(self):
        return self.image.url

class Activity(models.Model):
    participants = models.ManyToManyField(
        Profile,
        through='Participation',
        related_name='participant',
        )
    supervisors = models.ManyToManyField(
        Profile,
        related_name='supervisor',
        limit_choices_to={'account_type': 'LE'},
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


class Participation(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    participant = models.ForeignKey(Profile, on_delete=models.CASCADE)
    #supervisor = models.ForeignKey
    isVerified = models.BooleanField(default = False)

def activity_dir_path(instance, filename):
    return 'activity_{0}/{1}'.format(instance, filename)

class ActivityImage(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = activity_dir_path)

    def __str__(self):
        return self.image.upload_to
