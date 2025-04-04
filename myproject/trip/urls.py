# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.trip_list, name='trip_list'),  # Home page with list of trips
    path('book/<int:trip_id>/', views.book_trip, name='book_trip'),  # Book a specific trip
    path('booking_success/', views.booking_success, name='booking_success'),  # Success page
]
