from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import MovieListSerializer, MovieSerializer
from .models import Movie, Actor, Genre, Review
from accounts.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser




# 영화 목록 - TMDB 사용으로 필요 없음
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def movie_list(request):
    # 영화 목록 조회
    if request.method == 'GET':
        # movies = get_list_or_404(Movie)
        movies = Movie.objects.all()
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

    # # 영화 목록 수정(필요없음)
    # elif request.method == 'POST':
    #     serializer = MovieSerializer(data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         # serializer.save()
    #         serializer.save(user=request.user)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)


# 영화 상세 페이지 조회
@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(movie, pk=movie_pk)

    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        print(serializer.data)
        return Response(serializer.data)




# 닉네임
class CheckNicknameView(APIView):
    def get(self, request):
        nickname = request.query_params.get('nickname')
        if User.objects.filter(nickname=nickname).exists():
            return Response({'message': '이미 사용 중인 닉네임입니다.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': '사용 가능한 닉네임입니다.'}, status=status.HTTP_200_OK)

