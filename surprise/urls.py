from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('', views.home, name='home'),
    path('surprise/', views.surprise, name='surprise'),
    path('game/', views.game),
    path('countdown/', views.countdown),
    path('letter/', views.letter),
    path('slideshow/', views.slideshow),
    path('logout/', views.logout_page),
    path('loading/', views.loading),
]