from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm

# User = get_user_model()

# class SignupView(APIView):
#     def post(self, request):
#         form = CustomUserCreationForm(request.data)
#         if form.is_valid():
#             user = form.save()
#             return Response({'message': '회원가입 성공!'}, status=status.HTTP_201_CREATED)
#         return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
