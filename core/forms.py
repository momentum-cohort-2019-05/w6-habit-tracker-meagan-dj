from django import forms
import datetime
from django.contrib.auth.models import User

class DailyRecordForm(forms.Form):
    day_number = forms.IntegerField(help_text="Enter the day number for your habit")
    date = forms.DateField(initial=datetime.date.today, help_text="Enter the date")
    description = forms.CharField(help_text="Enter the description of your progress here")
    progress = forms.IntegerField(help_text="Enter your progress here")


class ObserverForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all())


class HabitForm(forms.Form):
    name = forms.CharField(max_length=300, help_text= "Enter your habit here")
    description = forms.CharField(help_text="Enter the decription of your habit here")
    target = forms.IntegerField(help_text = "Enter a target number for your habit")