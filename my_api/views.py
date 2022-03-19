from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from .models import School
from .serializers import SchoolSerializer


# Create your views here.

class SchoolInfoViewSet(ModelViewSet):
    # 指定查询集
    queryset = School.objects.all()

    # 指定序列化器
    serializer_class = SchoolSerializer
