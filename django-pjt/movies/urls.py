from django.urls import path
from . import views

app_name = "movies"
urlpatterns = [
    # 영화 데이터 가져오기
    path('movies/getdatas/', views.getdatas),
    # 영화 목록 조회
    path('movies/', views.movie_list),
    # 영화 상세 조회 
    path('movies/<int:movie_pk>/', views.movie_detail),
    # 영화 댓글 목록
    path('movies/comments', views.comment_list),
    # 영화 댓글 상세 조회
    path('movies/<int:movie_pk>/comments/<int:comment_pk>/', views.comment_detail),
    # 영화 댓글 제작
    path('movies/<int:movie_pk>/comments', views.comment_create),
    # 영화 좋아요
    path('movies/<int:movie_pk>/likemovies', views.like_movies),


]
