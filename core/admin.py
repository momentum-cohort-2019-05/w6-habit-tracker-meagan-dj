from django.contrib import admin
from core.models import Habit, Comment, Observer, DailyRecord


# Register your models here.
admin.site.register(Habit)
admin.site.register(Comment)
admin.site.register(Observer)
admin.site.register(DailyRecord)

