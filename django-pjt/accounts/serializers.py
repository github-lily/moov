from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import Movie
# from .models import Comment
from movies.serializers import MovieSerializer


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    # class MovieSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model = Movie
    #         fields = '__all__'

    # # 찜한 영화 
    # like_movies = MovieSerializer(source='user_like_movies', many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id','username', 'profile_img', 'like_movies','level')

# 프로필 이미지

class UserImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('profile_img', 'id')

# class CommentSerializer(serializers.ModelSerializer):
#     class UserSerializer(serializers.ModelSerializer):
#             class Meta:
#                 model = User
#                 fields = ('pk', 'username', 'profile_img')

#     user = UserSerializer(read_only=True)
#     class Meta:
#         model = Comment
#         fields = ('pk', 'user', 'content', 'profile', 'created_at',)
#         read_only_fields = ('profile',)
    