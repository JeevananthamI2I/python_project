
from django.contrib import admin  
from django.urls import path, include       
from authentication.views import *  
from django.conf import settings   
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('home/', home, name="recipes"),               
    path('login/', login_page, name='login_page'),    
    path('register/', register_page, name='register'), 
]


