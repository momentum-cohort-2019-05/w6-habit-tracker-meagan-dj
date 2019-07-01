from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Habit(models.Model):
    name = models.Charfield(max_length=300, help_text= "Enter your habit here")

