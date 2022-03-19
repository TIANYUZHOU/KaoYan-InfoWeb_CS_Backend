from django.shortcuts import render
from rest_framework.decorators import action
from django.http import FileResponse

from rest_framework.viewsets import ModelViewSet
from .models import School, Major, Material
from .serializers import SchoolSerializer, MaterialSerializer


# Create your views here.

class SchoolInfoViewSet(ModelViewSet):
    # 指定查询集
    queryset = School.objects.all()

    # 指定序列化器
    serializer_class = SchoolSerializer


class MaterialViewSet(ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

    @action(methods=['get', 'post'], detail=True)
    def download(self, request, pk=None, *args, **kwargs):
        file_obj = self.get_object()
        response = FileResponse(open(file_obj.file.path, 'rb'))
        return response
