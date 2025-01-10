# main/views.py
from django.shortcuts import render,redirect
from .models import Ride
from .forms import RideForm

# Home page
def home(request):
    return render(request, 'index.html')

# Create Ride page
def post_ride(request):
    if request.method == 'POST':
        # Handle the form submission and save ride
        form = RideForm(request.POST)
        if form.is_valid():
            ride = form.save(commit=False)
            ride.created_by = request.user
            ride.save()
            return redirect('view_rides')
    else:
        form = RideForm()
    return render(request,'createRide.html',{'form': form})
def view_rides(request):
    return render(request,'viewRide.html')
def contact_us(request):
    return render(request,'contact.html')
