from django.db import models
from django.contrib.auth.models  import User, Group

# Create your models here.

"""
class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.name

class CustomGroup(models.Model):
    group = models.OneToOneField(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.group.name
"""


class Device(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    serial = models.CharField(max_length=64, blank=False, unique=True)
    fw_version = models.CharField(max_length=64)
    dev_model = models.CharField(max_length=64)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

