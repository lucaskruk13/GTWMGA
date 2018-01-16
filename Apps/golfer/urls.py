from django.urls import path

from . import views

app_name = 'golfers'

urlpatterns = [
    # ex: /home/
    path('', views.MeetTheBoard, name='MeetTheBoard'),


]