from django.urls import path
from .views import book_create, book_list
urlpatterns = [ 
    path('', book_list, name='book_list'),
    path('create/', book_create, name='book_create'),
]