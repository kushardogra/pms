from os import name
from django.urls import path
from . import views
urlpatterns = [
    path('', views.signin, name='signin'),
    path('register', views.register, name='register'),
    # path('home', views.home,name='home'),
    path('add_coach',views.add_coach, name='add_coach'),
    path('add_player',views.add_player, name='add_player'),
    path('add_team',views.add_team, name='add_team'),
    path('team_profile',views.team_profile, name='team_profile'),
    path('coaches',views.coaches, name='coaches'),
    path('player_profile',views.player_profile, name='player_profile'),
    path('coach_profile',views.coach_profile, name='coach_profile'),
    path('player',views.player, name='player'),
    path('team',views.team, name='team'),
    path('logout', views.logout, name='logout'),
]