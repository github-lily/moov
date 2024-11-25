from rest_framework import serializers
from .models import Moviecomment, Movie, Genre, Actor, Director
from django.contrib.auth import get_user_model

User = get_user_model()

# 유저
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('pk','username', 'profile_img',)


# 장르
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields= '__all__'

# 배우
class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

# 감독
class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'

# 댓글
class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Moviecomment
        fields = '__all__'
        read_only_fields = ('user', 'movie')

# 영화
class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    actors = ActorSerializer(many=True)
    moviecomment_set = CommentSerializer(many=True, read_only=True)

    # 감독 이름
    class DirectorNameSerializer(serializers.ModelSerializer):
        class Meta:
            model = Director
            fields = ('name',)

    director = DirectorNameSerializer(read_only=True)

    class Meta:
        model = Movie
        fields='__all__'


# 영화 상세
class MovieDetailSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    moviecomment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='moviecomment_set.count', read_only=True)
    like_count = serializers.IntegerField(source='movie_like_users.count', read_only=True)
    genres = GenreSerializer(many=True)
    actors = ActorSerializer(many=True)
    
    class DirectorNameSerializer(serializers.ModelSerializer):
        class Meta:
            model = Director
            fields = ('name',)

    director = DirectorNameSerializer(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

        
class MovieListSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer) :
        class Meta:
            model = User
            fields = ('id','username')

    movie_like_users = UserSerializer(read_only=True, many=True)

    class Meta :
        model = Movie
        fields = ('id','title','movie_like_users')