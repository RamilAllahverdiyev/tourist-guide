from django.db import models
from django.contrib.auth.models import User


class City(models.Model):
    name = models.CharField(max_length=100)
    weather = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Destination(models.Model):
    name = models.CharField(max_length=100, default="")
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='destination_photos')
    description = models.TextField()
    history = models.TextField()

    def __str__(self):
        return f"{self.city.name} - {self.description[:20]}"
    

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.destination.description}"