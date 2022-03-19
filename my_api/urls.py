from django.urls import path

from rest_framework.routers import DefaultRouter
from .import views

urlpatterns = [

]

router = DefaultRouter()    # 创建路由器路由
router.register(r'',views.SchoolInfoViewSet) # 注册路由
urlpatterns += router.urls  # 把生成好饿路由拼接到 urlpatterns

