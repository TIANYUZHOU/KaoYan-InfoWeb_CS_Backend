from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import CreateUserSerializer
from .models import User


# Create your views here.

class UserView(CreateAPIView):
    """用户注册"""
    serializer_class = CreateUserSerializer


class UserNameCountView(APIView):
    """判断用户名是否已注册"""

    def get(self, request, username):
        # 查询user表
        count = User.objects.filter(username=username).count()

        # 响应数据
        data = {
            'username': username,
            'count': count
        }

        return Response(data)


class MobileCountView(APIView):
    """判断手机号是否已注册"""

    def get(self, request, mobile):
        # 查询user表
        count = User.objects.filter(mobile=mobile).count()

        # 响应数据
        data = {
            'username': mobile,
            'count': count
        }

        return Response(data)
