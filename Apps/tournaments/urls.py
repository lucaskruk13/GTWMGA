from django.urls import path

from . import views

app_name = 'tournaments'

urlpatterns = [
    # ex: /tournaments/
    path('', views.tournaments, name='tournaments'),
    path('<int:tournament_id>/', views.detail, name='detail'),
    path('<int:tournament_id>/gold_tee_results/', views.gold_tee_results, name='gold_tee_results'),
    path('<int:tournament_id>/blue_tee_results/', views.blue_tee_results, name='blue_tee_results'),
    path('<int:tournament_id>/black_tee_results/', views.black_tee_results, name='black_tee_results'),
    path('<int:tournament_id>/white_tee_results/', views.white_tee_results, name='white_tee_results'),
    path('point_standings/', views.point_standings, name='point_standings')
]