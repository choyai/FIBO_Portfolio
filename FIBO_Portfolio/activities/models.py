from django.db import models
from django.contrib.auth.models import User, Permission, Group
from profiles.models import Profile

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

    def get_absolute_url(selfself):
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
    return 'activity_{0}/{1}'.format(instance.acti)

class ActivityImage(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = activity_dir_path)
