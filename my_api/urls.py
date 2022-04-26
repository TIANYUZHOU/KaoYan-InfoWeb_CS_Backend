from django.urls import path

from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [

]

router = DefaultRouter()  # 创建路由器路由
# 注册路由
router.register('schools', views.SchoolInfoViewSet)
router.register('materials', views.MaterialViewSet)
router.register('majors', views.MajorInfoViewSet)
router.register('materialInfo', views.MaterialInfoViewSet)
router.register('collect', views.CollectViewSet)
router.register('links', views.LinkViewSet)
urlpatterns += router.urls  # 把生成好的路由拼接到 urlpatterns
