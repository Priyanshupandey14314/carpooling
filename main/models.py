from django.db import models

# Create your models here.
from django.contrib.auth.models import User  # For linking rides to users

class Ride(models.Model):
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    date = models.DateField()
    gender = models.CharField(max_length=10,
    choices = [('Male','Male'),('Female','Female'),('Any','Any')],default='Any')
    available_seats=models.IntegerField()
    price_per_seat =models.IntegerField()
    description = models.TextField(blank=True,null=True)
    created_by = models.ForeignKey('auth.user',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.source} to {self.destination} ({self.date})"

