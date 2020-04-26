from django.db import models

class User(models.Model):
    name = models.CharField(max_length=40)

class Manager(User):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=1000)

