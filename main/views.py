# main/views.py
from django.shortcuts import render
from .models import Ride

# Home page
def home(request):
    return render(request, 'index.html')

# Create Ride page
def create_ride(request):
    if request.method == 'POST':
        # Handle the form submission and save ride
        origin = request.POST['origin']
        destination = request.POST['destination']
        departure_time = request.POST['departure_time']
        available_seats = request.POST['available_seats']
        price_per_seat = request.POST['price_per_seat']
        description = request.POST['description']
        Ride.objects.create(
            driver=request.user,  # assuming user is logged in
            origin=origin,
            destination=destination,
            departure_time=departure_time,
            available_seats=available_seats,
            price_per_seat=price_per_seat,
            description=description
        )
    return render(request, 'createRide.html')

# View Rides page
def view_rides(request):
    rides = Ride.objects.all()
    return render(request, 'viewRide.html', {'rides': rides})
