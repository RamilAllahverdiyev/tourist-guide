from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('room/', views.room, name="room"),
    path('register/', views.register_page, name='register'),
    path('login', views.login_page, name='login'),
    path('profile/', views.profile_page, name='profile'),
    path('city/<int:city_id>/', views.city_details, name='city_details'),
    path('add_to_favorites/<int:destination_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('remove_from_favorites/<int:destination_id>/', views.remove_from_favorites, name='remove_from_favorites'),
]