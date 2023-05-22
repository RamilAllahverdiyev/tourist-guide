from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('room/', views.room, name="room"),
    path('register/', views.register_page, name='register'),
    path('login', views.login_page, name='login'),
    path('profile/', views.profile_page, name='profile'),
]