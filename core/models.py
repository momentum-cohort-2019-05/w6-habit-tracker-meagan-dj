from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Habit(models.Model):
    name = models.CharField(max_length=300, help_text= "Enter your habit here")
    description = models.TextField(help_text="Enter the decription of your habit here")
    target = models.IntegerField(help_text = "Enter a target number for your habit")
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    observers = models.ManyToManyField("Observer", blank=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.name
                                        

class DailyRecord(models.Model):
    day_number = models.IntegerField(help_text = "Enter the day number for your habit")
    date = models.DateField(help_text = "Enter the date")
    description = models.TextField(help_text="Enter the description of your progress here")
    progress = models.IntegerField(help_text = "Enter your progress here")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['habit', 'date']]

    def __str__(self):
        """String for representing the Model object."""
        return self.date 


class Comment(models.Model):
    description = models.TextField(help_text="Enter your comment here")
    observer = models.ForeignKey("Observer", on_delete=models.CASCADE)
    daily_record = models.ForeignKey(DailyRecord, on_delete=models.CASCADE)


class Observer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        """String for representing the Model object."""
        return self.user.username





