# main/views.py
from django.shortcuts import render,redirect
from .models import Ride
from django.contrib import messages
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from .forms import RideForm
from django.contrib.auth.models import User
from django.views.decorators.http import require_GET
from django.core.serializers import serialize
from django.forms.models import model_to_dict
# Home page
def home(request):
    return render(request, 'index.html')
# create_ride handling manually
'''def offer_ride(request):
    if request.method == 'POST':
        # manually saving the data
        try:
            source = request.POST.get('source')
            destination = request.POST.get('destination')
            date = request.POST.get('date')
            gender = request.POST.get('gender')
            available_seats = request.POST.get('available_seats')
            price_per_seat = request.POST.get('price_per_seat')
            description = request.POST.get('description', '')
            driver_name = request.POST.get('driver_name')
            driver_phone = request.POST.get('driver_phone')

            # Create and save the ride
            Ride.objects.create(
                source=source,
                destination=destination,
                date=date,
                gender=gender,
                available_seats=available_seats,
                price_per_seat=price_per_seat,
                description=description,
                created_by=request.user,
                driver_name=driver_name,
                driver_phone=driver_phone,
            )

            messages.success(request, "Ride offered successfully!")
            return redirect('find_ride')

        except Exception as e:
            messages.error(request, f"Error: {e}")
            return redirect('offer_ride')

    return render(request, 'createRide.html')'''
# Create ride with moedlForms
def offer_ride(request):
    test_user = User.objects.get(username="Priyanshu")
    if request.method == 'POST':
        form = RideForm(request.POST)
        if form.is_valid():
            ride = form.save(commit=False)
            ride.created_by = test_user
            ride.save()
            messages.success(request, "Ride offered successfully!")
            # return redirect('find_ride')
    else:
        form = RideForm()
    return render(request, 'createRide.html', {'form': form})

# find ride handling 
@require_GET
def find_ride(request):
     source = request.GET.get('source')
     destination= request.GET.get('destination')
     date = request.GET.get('date')
     rides = Ride.objects.all()
     if source:
         rides = rides.filter(source=source)
     if destination:
         rides = rides.filter(destination=destination)
     if date:
         rides = rides.filter(date=date)
     context = {
         'rides': rides,
         'source': source or '',
         'destination': destination or '',
         'date': date or ''
     }
     return render(request, 'viewRide.html', context)
def contact_us(request):
    return render(request,'contact.html')
