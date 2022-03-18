from django.apps import AppConfig


class MyApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'my_api'
    verbose_name = 'API表管理'
