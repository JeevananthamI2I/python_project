from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib import admin

# 1. User Model (Custom)
class User(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)
    is_driver = models.BooleanField(default=False)  # Check if the user is a driver

# 2. Vehicle Model
class Vehicle(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle_type = models.CharField(max_length=50)  # Car, Bike, Auto, etc.
    registration_number = models.CharField(max_length=20, unique=True)
    model = models.CharField(max_length=100)
    capacity = models.IntegerField()  # Seats available

# 3. Trip Model
class Trip(models.Model):
    driver = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_driver': True})
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    start_location = models.CharField(max_length=255)
    end_location = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_completed = models.BooleanField(default=False)

# 4. Booking Model
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    seats_booked = models.IntegerField()
    booking_time = models.DateTimeField(auto_now_add=True)
    is_confirmed = models.BooleanField(default=False)

# 5. Admin Registration
admin.site.register(User)
admin.site.register(Vehicle)
admin.site.register(Trip)
admin.site.register(Booking)
