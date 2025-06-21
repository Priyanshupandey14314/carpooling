from django.contrib import admin
from .models import Ride
# Register your models here.
@admin.register(Ride)
class RideAdmin(admin.ModelAdmin):
    list_display = ('source', 'destination', 'date', 'available_seats', 'price_per_seat', 'created_by', 'driver_name')
    list_filter = ('date', 'gender', 'source', 'destination')
    search_fields = ('source', 'destination', 'driver_name', 'created_by__username')