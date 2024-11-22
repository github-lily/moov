from django.shortcuts import get_object_or_404, get_list_or_404
from django.http import JsonResponse
from django.conf import settings
from django.contrib.auth import get_user_model
import requests, json


from .serializers import MovieDetailSerializer, MovieSerializer, CommentSerializer
from .models import Movie, Actor, Genre, Moviecomment
from accounts.models import User


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser


TMDB_URL = 'https://api.themoviedb.org/3/'
TMDB_API_KEY = settings.TMDB_API_KEY


# api_key로 데이터 받아오기
@api_view(['GET'])
def getdatas():

    # 전체 데이터
    total_list = []
    
    # 장르 받아오기
    genre_url = f"{TMDB_URL}genre/movie/list?api_key={TMDB_API_KEY}&language=ko-KR"
    genres = requests.get(genre_url).json()
    for genre in genres['genres']:
        fields = {
            'name':genre['name']
        }

        genre = {
            'model': 'movies.Genre',
            'pk': genre['id'],
            'fields': fields
        }
        total_list.append(genre)



    # 영화데이터 받아오기
    # for i in range(1, 300): # 몇 페이지까지 받아올지
    for i in range(1, 200):
        movie_url = f"{TMDB_URL}movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        movies = requests.get(movie_url).json()

        for movie in movies['results']:
            # 값이 있다면 가져오기()
            if movie.get('release_date', '') and (movie.get('overview') != '' and movie.get('poster_path') != None and movie.get('release_date') != None):
                # 영화 상세 정보
                movie_detail_url = f"{TMDB_URL}movie/{movie['id']}?api_key={TMDB_API_KEY}&language=ko-KR"
                movie_detail = requests.get(movie_detail_url).json()
                # 배우, 감독 정보
                movie_people_url = f"{TMDB_URL}movie/{movie['id']}/credits?api_key={TMDB_API_KEY}&language=ko-KR"
                movie_people = requests.get(movie_people_url).json()
                # 예고편 정보
                movie_trailer_url = f"{TMDB_URL}movie/{movie['id']}/videos?api_key={TMDB_API_KEY}&language=ko-KR"
                movie_trailer = requests.get(movie_trailer_url).json()
                # print(movie_trailer)

                actors = []
                actor_list = []
                if len(movie_people['cast']) < 7:
                    for i in range(len(movie_people['cast'])):
                        actors.append(movie_people['cast'][i]['id'])
                        actor_list.append(movie_people['cast'][i])
                else:
                    for i in range(7):
                        actors.append(movie_people['cast'][i]['id'])
                        actor_list.append(movie_people['cast'][i])

                director = ''
                director_list = []
                for direct in movie_people['crew']:
                    if direct['department'] == 'Directing':
                        director = direct['id']
                        director_list.append(direct)
                        break
                print(director)

                # 영화에 출연한 배우 받아오기
                for actor in actor_list:
                    fields = {
                        'name':actor['name']
                    }
                    actor = {
                        'model': 'movies.Actor',
                        'pk': actor['id'],
                        'fields': fields
                    }
                    total_list.append(actor)

                # 영화 만든 감독 받아오기
                if director_list:
                    fields = {
                        'name':director_list[0]['name']
                    }
                    directors = {
                        'model': 'movies.Director',
                        'pk': director_list[0]['id'],
                        'fields': fields
                    }
                    total_list.append(directors)

                # 영화 정보 받아오기
                if director_list and movie_trailer['results']:
                    fields = {
                        'title': movie['title'],
                        'overview': movie['overview'],
                        'release_date': movie['release_date'],
                        'poster_path': movie['poster_path'],
                        'trailer_key': movie_trailer['results'][0]['key'],
                        'runtime': movie_detail['runtime'],
                        'genres': movie['genre_ids'],
                        'actors': actors,
                        'director': director,
                        'adult': movie['adult'],
                        # 'popularity': movie['popularity'],
                        'vote_count': movie['vote_count'],
                        'vote_average': movie['vote_average'],
                        'original_language': movie['original_language'],
                        'movie_like_users': [],
                    }
                    movie = {
                        'model': 'movies.Movie',
                        'pk': movie['id'],
                        'fields': fields
                    }
                    total_list.append(movie)


    # 파일 없을 경우 만들기
    directory = "fixtures"
    if not os.path.exists(directory):
        os.makedirs(directory)


    # JSON 파일 생성
    with open(f"{directory}/datas.json", "w", encoding="utf-8") as w:
        json.dump(total_list, w, indent=4, ensure_ascii=False)

    print(f"{directory}/datas.json 파일이 성공적으로 생성되었습니다.")


# getdatas()



# 영화 목록 조회
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)



# 영화 상세 페이지 조회
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    # if request.method == 'GET':
    serializer = MovieSerializer(movie)
    return Response(serializer.data)




# 영화 댓글 생성
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
# 영화 상세정보에서 댓글 조회, 삭제, 수정
@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def comment_detail(request,  movie_pk, comment_pk):
    comment = get_object_or_404(Moviecomment, pk=comment_pk, movie_id=movie_pk)
    
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        if request.user != comment.user:
            return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        if request.user != comment.user:
            return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


# 영화를 좋아요 한 사람 목록
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_movies(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if movie.movie_like_users.filter(pk=request.user.pk).exists():
        movie.movie_like_users.remove(request.user)
    else:
        movie.movie_like_users.add(request.user)
    return Response(status=status.HTTP_200_OK)


User = get_user_model()

# 좋아요 누른 모든 영화 반환
@api_view(['GET'])
def like_movies_list(request, username):
    user = get_object_or_404(User, username=username)
    movies = user.user_like_movies.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


# ========================================================================
# MyPage 영화 댓글 조회 관련 부분


# # 영화 전체 댓글 조회
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def comment_list(request):
#     # comments = Moviecomment.objects.filter(movie_id=movie_pk)
#     comments = Moviecomment.objects.all()
#     serializer = CommentSerializer(comments, many=True)
#     return Response(serializer.data)


# 사용자가 댓글 단 영화 목록 조회
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def commented_movies(request):
    comments = Moviecomment.objects.filter(user=request.user).select_related('movie')
    movies = set(comment.movie for comment in comments)
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


# 사용자가 댓글 단 영화 목록
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_list(request, movie_pk, comment_pk):
    movie = get_object_or_404(Movie, movie_pk=movie_pk)
    comment = get_object_or_404(Movie, movie_pk=movie_pk, comment_pk=comment_pk)
    serializer = CommentSerializer(comment, many=True)
    return Response(serializer.data)



# 사용자가 댓글 단 영화 목록 조회
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_commented_movies(request):
    comments = Moviecomment.objects.filter(user=request.user).select_related('movie')
    movies = set(comment.movie for comment in comments)
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)