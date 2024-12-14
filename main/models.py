from django.db import models

# Create your models here.
from django.contrib.auth.models import User  # For linking rides to users

class Ride(models.Model):
    driver = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to User model
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    departure_time = models.DateTimeField()
    available_seats = models.IntegerField()
    price_per_seat = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return f"{self.origin} to {self.destination} ({self.departure_time})"
