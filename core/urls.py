from django.urls import path
from . import views

urlpatterns = [
    # User can view all their Habits --> '/' that redirects to '/habits/' - DJ
    path('habits/', views.list_habits, name='habit-list'),
    # User can create a new Habit --> '/habits/create/' - DJ
    path('habits/new-habit/', views.create_habit, name='create-habit'),
    path('habits/<int:pk>/', views.habit_detail, name='habit-detail'),
    # User can add a DailyRecord to a Habit --> '/habits/<int:pk>/new-record/' - DJ
    path('habits/<int:pk>/new-record/', views.create_daily_record, name='create-daily-record'),
    # User can edit a DailyRecord --> '/dailyrecords/<int:pk>/' -- Meagan
    path('dailyrecords/<int:pk>/', views.EditDailyRecord.as_view(), name='daily-record-edit'),
    path('habits/<int:pk>/new-observer/', views.create_observer, name='create-observer'),
    path('', views.index, name='index'),
]