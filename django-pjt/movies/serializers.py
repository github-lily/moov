from rest_framework import serializers
from .models import Moviecomment, Movie, Genre, Actor, Director

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields= '__all__'


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Moviecomment
        fields = '__all__'
        read_only_fields = ('user', 'movie',)

class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    actors = ActorSerializer(many=True)
    moviecomment_set = CommentSerializer(many=True, read_only=True)

    class DirectorNameSerializer(serializers.ModelSerializer):
        class Meta:
            model = Director
            fields = ('name',)

    director = DirectorNameSerializer(read_only=True)

    class Meta:
        model = Movie
        fields='__all__'



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