from django.db import models
from django.conf import settings

# Create your models here.

class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

class Actor(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

class Director(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)


class Movie(models.Model) :
    id = models.IntegerField(primary_key=True)
    actors = models.ManyToManyField(Actor)
    adult = models.BooleanField(default=False)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre)
    title = models.CharField(max_length=100)
    overview = models.TextField()
    popularity = models.FloatField(null=True, blank=True)
    poster_path = models.CharField(max_length=200)
    release_date = models.DateField()
    runtime = models.IntegerField() 
    trailer_key = models.CharField(max_length=200)
    vote_count = models.IntegerField(default=0)
    vote_average = models.FloatField(default=0.0)
    movie_like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='user_like_movies', blank=True)
    original_language = models.CharField(max_length=50, null=True)
    



class Moviecomment(models.Model) :
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)    # 댓글 쓴 사람
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')  # 영화와 연결
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
