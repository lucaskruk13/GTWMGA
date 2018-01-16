from django.urls import path

from . import views

app_name = 'mga_home'

urlpatterns = [
    # ex: /home/
    path('', views.index, name='index'),

]