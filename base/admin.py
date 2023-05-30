from django.contrib import admin

from .models import City, Destination, Favorite

admin.site.register(City)
admin.site.register(Destination)
admin.site.register(Favorite)

