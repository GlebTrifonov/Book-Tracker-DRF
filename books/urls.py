from django.urls import path
from .views import book_create, book_list, book_toggle, book_delete
from .api_view import BookDetailAPIView, BookListAPIView



urlpatterns = [ 
    path('', book_list, name='book_list'),
    path('create/', book_create, name='book_create'),
    path('<int:pk>/toggle/', book_toggle, name='book_toggle'),
    path('<int:pk>/delete/', book_delete, name='book_delete'),
    path('api/v1/list/', BookListAPIView.as_view(), name='api_habit_list'),
    path('api/v1/<int:pk>/', BookDetailAPIView.as_view(), name='api_habit_detail'),
]