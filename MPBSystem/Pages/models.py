from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin


class Displaynames(models.Model):
    username = models.CharField(max_length=100)


class Dashboard(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    is_superuser = models.BooleanField(default=False)

