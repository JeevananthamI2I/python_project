from django.urls import path
from . import views

urls =[
    path('', views.upload_file, name='upload_file'),  # List of authors
    # path('author/<int:pk>/', views.author_list, name='author_detail'),  # Author detail page
]