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