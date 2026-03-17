from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'user', 'title', 'author', 'genre', 'rating', 'created_at', 'status']
        read_only_fields = ['user', 'created_at','status']