from django.urls import path
from . import views

urlpatterns = [
    # 프로필 페이지
    path('mypage/<username>/', views.user_profile),
    # 프로필 이미지
    path('upload_img/<username>/', views.upload_img),

    # path('follow/<username>/', views.follow),
]