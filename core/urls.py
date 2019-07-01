from django.urls import path
from . import views

urlpatterns = [
    path('habits/', views.list_habits, name='habit-list'),
    path('habits/<int:pk>/', views.habit_detail, name='habit-detail'),
]