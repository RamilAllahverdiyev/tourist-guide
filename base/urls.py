from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home, name='home'),
    path('room/', views.room, name="room"),
    path('register/', views.register_page, name='register'),
    path('login', views.login_page, name='login'),
    path('profile/', views.profile_page, name='profile'),
    path('city/<int:city_id>/', views.city_details, name='city_details'),
    path('add_to_favorites/<int:destination_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('remove_from_favorites/<int:destination_id>/', views.remove_from_favorites, name='remove_from_favorites'),
    path('search/', views.search_view, name='search'),
    path('help/', views.help_page, name='help'),
    path('logout/', views.logout_page, name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)