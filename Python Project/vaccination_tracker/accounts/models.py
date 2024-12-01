
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_parent = models.BooleanField(default=False)
    is_facilitator = models.BooleanField(default=False)

class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    parent_id = models.CharField(max_length=100, unique=True)

class Facilitator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    secret_key = models.CharField(max_length=50)
    

