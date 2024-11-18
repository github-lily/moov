from django.db import models
from django.conf import settings

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=50)

class Actor(models.Model):
    name = models.CharField(max_length=50)

class Movie(models.Model) :
    # 영화 리스트에는 굳이 안필요함
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    overview = models.TextField(blank=True)
    release_date = models.DateTimeField(blank=True)
    level = models.IntegerField(blank=True)
    poster_path = models.CharField(max_length=200, blank=True)
    runtime = models.IntegerField(blank=True, null=True)       # 분 단위로 저장 # null=True: 데이터베이스에서 NULL 값을 허용한다는 의미.
    genres = models.ManyToManyField(Genre)
    actors = models.ManyToManyField(Actor)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')


class Review(models.Model) :
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
