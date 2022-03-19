from django.urls import path

from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [

]

router = DefaultRouter()  # 创建路由器路由
# 注册路由
router.register(r'schools', views.SchoolInfoViewSet)
router.register(r'materials', views.MaterialViewSet)
urlpatterns += router.urls  # 把生成好饿路由拼接到 urlpatterns
