from django.urls import path, re_path
from rest_framework.routers import DefaultRouter

from . import views
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView, TokenObtainPairView

urlpatterns = [
    path('users/', views.UserView.as_view()),
    re_path(r'^users/(?P<username>\w{5,20})/count/$', views.UserNameCountView.as_view()),
    re_path(r'^mobiles/(?P<mobile>1[3-9]\d{9})/count/$', views.MobileCountView.as_view()),
    # path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("login/", views.LoginView.as_view()),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("verify/", TokenVerifyView.as_view(), name="token_verify"),
]

router = DefaultRouter()  # 创建路由器路由
router.register('userprofile', views.UsersProfileViewSet)
urlpatterns += router.urls
