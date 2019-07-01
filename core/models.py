from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Habit(models.Model):
    name = models.Charfield(max_length=300, help_text= "Enter your habit here")
    description = models.TextField(help_text="Enter the decription of your habit here")
    target = models.IntegerField(help_text = "Enter a target number for your habit")


class DailyRecord(models.Model):
    day_number = models.IntegerField(help_text = "Enter the day number for your habit")
    date = models.DateField(help_text = "Enter the date")
    description = models.TextField(help_text="Enter the description of your progress here")
    progress = models.IntegerField(help_text = "Enter your progress here")


class Comment(models.Model):
    description = models.TextField(help_text="Enter your comment here")


class Observer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)




