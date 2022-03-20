from django.shortcuts import render
from rest_framework.decorators import action
from django.http import FileResponse

from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .models import School, Major, Material
from .serializers import SchoolSerializer, MaterialSerializer, MajorSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination


# Create your views here.

# 分页
class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000  # 默认每页显示多少条
    page_query_param = 'page'  # 请求第 n 页时的关键字
    page_size_query_param = 'page_size'  # 请求每页条数的关键字
    max_page_size = 10000 # 最大每页请求条数


class SchoolInfoViewSet(ReadOnlyModelViewSet):
    # 指定查询集
    queryset = School.objects.all()

    # 指定序列化器
    serializer_class = SchoolSerializer


class MajorInfoViewSet(ReadOnlyModelViewSet):
    # 指定查询集
    queryset = Major.objects.all()

    # 指定序列化器
    serializer_class = MajorSerializer


class MaterialViewSet(ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

    # 只有登录用户才能访问此视图
    permission_classes = [IsAuthenticated]

    # 指定过滤字段为排序过滤
    filter_backends = [OrderingFilter]

    # 允许过滤（搜索）的字段
    filter_fields = ['id', 'matName', 'user', 'school']

    # 分页
    pagination_class = LargeResultsSetPagination

    @action(methods=['get', 'post'], detail=True)
    def download(self, request, pk, *args, **kwargs):
        file_obj = self.get_object()
        # print(file_obj)
        response = FileResponse(open(file_obj.file.path, 'rb'))
        return response
