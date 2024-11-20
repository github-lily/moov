from django.urls import path
from . import views

app_name = "movies"
urlpatterns = [
    # 영화 목록 조회
    path('movies/', views.movie_list),
    # 영화 상세 조회 
    path('movies/<int:movie_pk>/', views.movie_detail),
    # 영화 데이터 가져오기
    path('movies/getdatas/', views.getdatas),
    # 댓글 조회 및 생성
    path('movies/<int:movie_pk>/comments/', views.comment_list_create),


]
