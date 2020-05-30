from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
import uuid


# Create your models here.
class User(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, blank=False)
    tz = models.DateField()

    def __str__(self):
        return self.name


class ActivityPeriod(models.Model):
    activityby = models.ForeignKey('User', on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return ''

