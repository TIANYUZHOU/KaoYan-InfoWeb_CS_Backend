"""gra_design_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,re_path
from django.urls import include
from rest_framework.documentation import include_docs_urls

from gra_design_backend import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('my_api.urls')),
    path('docs/', include_docs_urls(title='My API title')),
    re_path(r'^',include('verification.urls')),  # 发短信
    re_path(r'^',include('user.urls'))
]

# 主路由中：显性告诉django绑定media_url和media_root
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)