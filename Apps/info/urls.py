from django.urls import path

from . import views

app_name = 'info'

urlpatterns = [
    # ex: /home/
    path('bylaws/', views.bylaws, name='ByLaws'),


]