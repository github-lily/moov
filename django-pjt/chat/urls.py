from django.urls import path
from . import views

urlpatterns = [
    path('stream-chat/', views.stream_chat, name='stream_chat'),
]
