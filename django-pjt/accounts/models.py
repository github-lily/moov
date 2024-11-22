from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser) :
    # username = models.CharField(max_length=30, unique=True) 기본 제공 필드
    # 프로필 이미지
    profile_img = models.TextField(blank=True)