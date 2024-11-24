from rest_framework import status
from rest_framework.decorators import api_view, permission_classes

from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model
from django.http import JsonResponse

from rest_framework.response import Response
from .serializers import UserSerializer, UserImgSerializer
from movies.serializers import MovieSerializer
from rest_framework.authentication import TokenAuthentication, BasicAuthentication


from movies.serializers import MovieSerializer
from movies.models import Movie

# from .models import Comment, Profile



# 이미지 업로드
@api_view(['GET', 'PUT'])
def upload_img(request, user_id):
    user = get_object_or_404(get_user_model(), username=user_id)

    # 프로필 사진 조회
    if request.method == 'GET':
        serializer = UserImgSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 프로필 사진 수정
    elif request.method == 'PUT':
        if request.user != user:
            return Response({'profile':'권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)

        serializer = UserImgSerializer(user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)


# 프로필 페이지 조회
@api_view(['GET'])
def user_profile(request, user_id):
    user = get_object_or_404(get_user_model(), id=user_id)
    if request.method == 'GET':
        user_serializer = UserSerializer(user)
        # data = {
        #     'user' : user_serializer.data,
        # }
        return Response(user_serializer.data)
    
    


# @api_view(['POST'])
# def comment_create(request, username):
#     profile = get_object_or_404(Profile, username=username)
    
#     serializer = CommentSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save(profile=profile, user=request.user)
#         comments = profile.comments.all()
#         serializer = CommentSerializer(comments, many=True)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

# @api_view(['POST'])
# def follow(request, username):
#     user = get_object_or_404(get_user_model(), username=username)
#     if user != request.user:
#         if user.followers.filter(pk=request.user.pk).exists():
#             user.followers.remove(request.user)
#             followed = False
#         else:
#             user.followers.add(request.user)
#             followed = True
#     context = {
#         'followed' : followed,
#     }
#     # return Response(context, status=status.HTTP_200_OK)
#     serializer = UserSerializer(user)
#     return Response(serializer.data)

