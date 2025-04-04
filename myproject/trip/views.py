# views.py
from django.shortcuts import render
from .models import Trip
from django.shortcuts import render, get_object_or_404, redirect
from .models import Trip, Booking
from django import forms
from .models import Booking

def trip_list(request):
    trips = Trip.objects.all()  # Fetch all trips
    return render(request, 'trips/trip_list.html', {'trips': trips})

# views.py

def book_trip(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id)
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user 
            booking.trip = trip
            booking.save()
            return redirect('booking_success')
    else:
        form = BookingForm()
    
    return render(request, 'trips/book_trip.html', {'form': form, 'trip': trip})

# views.py

def booking_success(request):
    return render(request, 'trips/booking_success.html')


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['status']