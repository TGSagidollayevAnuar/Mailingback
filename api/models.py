from django.db import models

class User(models.Model):
    name = models.CharField(max_length=40)

class Manager(User):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=1000)

class Mail(models.Model):
    title = models.CharField(max_length=40)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="author")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="receiver")
 
class Draft(models.Model):
    title = models.CharField(max_length=40)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)    
