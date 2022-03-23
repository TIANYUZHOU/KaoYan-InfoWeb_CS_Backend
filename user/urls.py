from django.urls import path, re_path

from . import views

urlpatterns = [
    path('users/', views.UserView.as_view()),
    re_path(r'^users/(?P<username>\w{5,20})/count/$', views.UserNameCountView.as_view()),
    re_path(r'^mobiles/(?P<mobile>1[3-9]\d{9})/count/$', views.MobileCountView.as_view()),
]
