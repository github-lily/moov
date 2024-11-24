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


    # 영화 댓글 생성
    path('movies/<int:movie_pk>/comments/', views.comment_create),
    # 영화 댓글 조회&수정&삭제
    path('movies/<int:movie_pk>/comments/<int:comment_pk>/', views.comment_detail),
    # 사용자가 댓글 단 영화 목록 조회
    path('movies/<str:username>/comments/', views.user_commented_movies),

    
    # 영화 좋아요
    path('movies/<int:movie_pk>/likemovies', views.like_movies),
    # 좋아요 누른 영화 목록 조회
    path('mypage/<int:user_id>/likemovieslist/', views.like_movies_list, name='like_movies_list'),



]
