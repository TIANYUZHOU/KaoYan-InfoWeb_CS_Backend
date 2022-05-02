"""
Django settings for gra_design_backend project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import datetime
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1v)^^bd29e+wl!q3omu7&y+6u=zmhz^p&lz4sw&wu=pvd&a61$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'simpleui',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    "corsheaders",
    'django_filters',

    # 自定义 app
    'my_api.apps.MyApiConfig',
    'user'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'gra_design_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'django.template.context_processors.media'
            ],
        },
    },
]

WSGI_APPLICATION = 'gra_design_backend.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'KaoYanWeb_CS',
        'USER': 'root',
        'PASSWORD': '1183380395',
        'HOST': '127.0.0.1',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_PROFILE_MODULE = 'djangoadmin.myadmin.UserExtend'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 跨域允许的请求方式，可以使用默认值，默认的请求方式为:
# from corsheaders.defaults import default_methods
CORS_ALLOW_METHODS = (
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS'
)

# 允许跨域的请求头，可以使用默认值，默认的请求头为:
# from corsheaders.defaults import default_headers
# CORS_ALLOW_HEADERS = default_headers

CORS_ALLOW_HEADERS = (
    'XMLHttpRequest',
    'X_FILENAME',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'Pragma',
)

# 跨域请求时，是否运行携带cookie，默认为False
CORS_ALLOW_CREDENTIALS = True
# 允许所有主机执行跨站点请求，默认为False
# 如果没设置该参数，则必须设置白名单，运行部分白名单的主机才能执行跨站点请求
CORS_ORIGIN_ALLOW_ALL = True

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework_jwt.authentication.JSONWebTokenAuthentication',  # JWT
        'rest_framework_simplejwt.authentication.JWTAuthentication',  # 使用rest_framework_simplejwt验证身份
        'rest_framework.authentication.BasicAuthentication',  # 基本认证
        'rest_framework.authentication.SessionAuthentication',  # session认证
    ),
    # 限流配置
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '500/second',
        'user': '500/second'
    },
    # 过滤器
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    # 分页
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # 接口文档
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
}

# 修改 Django 默认用户模型
AUTH_USER_MODEL = 'user.User'

# JWT 配置
# JWT_AUTH = {
#     'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),  # JWT有效期
# }

SIMPLE_JWT = {
    # token有效时长
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(days=1),
    # token刷新后的有效时间
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=1),
    # 更新last_login字段
    'UPDATE_LAST_LOGIN': True
}

# 修改默认认证后端
AUTHENTICATION_BACKENDS = ['user.utils.UserNameMobileAuthBackend',
                           ]
# 隐藏右侧SimpleUI广告链接和使用分析
SIMPLEUI_HOME_INFO = False
# SIMPLEUI_ANALYSIS = False
SIMPLEUI_LOGO = 'https://pic.zty.plus/Logo/back_logo.png'
SIMPLEUI_DEFAULT_THEME = 'dark.green.css'
# SIMPLEUI_ICON = {
#     '仓库信息表': 'fas fa-warehouse',
#     '入库表': 'fas fa-sign-in-alt',
#     '出库表': 'fas fa-sign-out-alt'
# }
# SIMPLEUI_HOME_PAGE = 'http://127.0.0.1:8000/admin/'
# SIMPLEUI_HOME_TITLE = '作者博客'
# SIMPLEUI_CONFIG = {
#     # 'system_keep': False, # 关闭系统菜单
#     # 'menu_display': ['仓库管理'],
#     'dynamic': True,  # 设置是否开启动态菜单, 默认为False. 如果开启, 则会在每次用户登陆时动态展示菜单内容
#     'menus': [{
#         'app': 'my_api',
#         'name': 'API管理',
#         'icon': 'fas fa-tasks',
#         'models': [{
#             'name': '院校表',
#             'icon': 'fas fa-warehouse',
#             'url': 'admin/my_api/school/'
#         }, {
#             'name': '入库表',
#             'icon': 'fas fa-sign-in-alt',
#             'url': 'backend/instock/'
#         }, {
#             'name': '出库表',
#             'icon': 'fas fa-sign-out-alt',
#             'url': 'backend/outofstock/'
#         }, {
#             'name': '货物信息表',
#             'icon': 'fab fa-product-hunt',
#             'url': 'backend/product/'
#         }, {
#             'name': '工作人员表',
#             'icon': 'fas fa-male',
#             'url': 'backend/staff/'
#         }]
#     }, {'app': 'auth',
#         'name': '用户管理',
#         'icon': 'fas fa-user-shield',
#         'models': [
#             {
#                 'name': '用户',
#                 'icon': 'fa fa-user',
#                 'url': 'auth/user/'
#             },
#             {
#                 'name': '用户组',
#                 'icon': 'fas fa-users-cog',
#                 'url': 'auth/group/'
#             }
#         ]
#         }]
# }
SIMPLEUI_ICON = {
    '专业': 'fas fa-book',
    '资料': 'fas fa-folder-open',
    '院校': 'fas fa-university',
    '用户': 'fas fa-users',
    '反馈': 'fas fa-comments'
}
