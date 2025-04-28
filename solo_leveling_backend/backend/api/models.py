from django.db import models

# Create your models here.



class UserProfile(models.Model):
    curr_xp = models.IntegerField(default=0)
    next_xp = models.IntegerField(default = 100)
    level = models.IntegerField(default = 1)
    date_created = models.DateField(auto_now_add=True)
    #foreign key to actual user account.


class Task(models.Model):
    heading = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    finished = models.BooleanField(default=False)
    priority = models.IntegerField(default=1)
    #foreign key to actual user account.

class Achievement(models.Model):
    name = models.CharField(max_length=100)
    date_achieved = models.DateField(auto_now_add=True)
    description = models.TextField(max_length=300)
    #Foreign key to actual user.



