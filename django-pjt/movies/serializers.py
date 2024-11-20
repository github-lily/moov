from rest_framework import serializers
from .models import Moviecomment, Movie

# 영화 목록
class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'overview','poster_path')


# 전체 영화
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('user',)

# 리뷰
class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # 유저 이름을 문자열로 표시
    class Meta:
        model = Moviecomment
        fields = '__all__'
