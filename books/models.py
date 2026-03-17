from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models



class Book(models.Model):
    class Genre(models.TextChoices):
        HORROR = 'horror', 'Horror'
        SCIENCE = 'science', 'Science'
        DRAMA = 'drama', 'Drama'
        SATIRE = 'satire', 'Satire'
        HISTORY = 'history', 'History'
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')
    title = models.CharField(max_length=200, verbose_name='название книги')
    author = models.CharField(max_length=200, verbose_name='автор')
    genre = models.CharField(max_length=50, choices=Genre.choices, verbose_name='Жанр')
    status = models.BooleanField(default=False, verbose_name='Прочитано/Не прочитано')
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1, message='Рейтинг не может быть ниже 1'),
            MaxValueValidator(5, message='Рейтинг не может быть выше 5')
        ],
        verbose_name='Рейтинг книги'
    )
    review = models.TextField(blank=True, null=True, verbose_name='Отзыв')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        ordering = ['-created_at']