from django.db import models

# Create your models here.

class Review(models.Model):
    GENRE_CHOICES = [
        ('action', 'Action'),
        ('comedy', 'Comedy'),
        ('drama', 'Drama'),
        ('fantasy', 'Fantasy'),
        ('horror', 'Horror'),
        ('romance', 'Romance'),
        ('sci-fi', 'Sci-Fi'),
        ('thriller', 'Thriller'),
    ]

    title = models.TextField()
    director = models.TextField()
    main_actor = models.TextField()
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    rating = models.PositiveIntegerField()
    running_time = models.PositiveIntegerField()
    content = models.TextField()

    release_year = models.PositiveIntegerField()
