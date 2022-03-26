from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import CreateUserSerializer
from .models import User

from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenViewBase

from .serializers import MyTokenSerializer


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
            'mobile': mobile,
            'count': count
        }

        return Response(data)


# 自定义的登陆视图
class LoginView(TokenViewBase):
    serializer_class = MyTokenSerializer  # 使用刚刚编写的序列化类

    # post方法对应post请求，登陆时post请求在这里处理
    def post(self, request, *args, **kwargs):
        # 使用刚刚编写时序列化处理登陆验证及数据响应
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            raise ValueError(f'验证失败： {e}')

        return Response(serializer.validated_data, status=status.HTTP_200_OK)