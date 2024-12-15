# main/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('createRides/', views.create_ride, name='createRide'),  # Page to create a ride
    path('viewRides/', views.view_rides, name='viewRide'),  # Page to view available rides
]
