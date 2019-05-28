from django.db import models

# Create your models here.


class user(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    usergroup = models.CharField(max_length=20)
class device(models.Model):
    ip = models.CharField(max_length=30)
    hostname = models.CharField(max_length=50)
