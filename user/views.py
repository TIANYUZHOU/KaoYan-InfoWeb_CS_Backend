from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .serializers import CreateUserSerializer


# Create your views here.

class UserView(CreateAPIView):
    """用户注册"""
    serializer_class = CreateUserSerializer
