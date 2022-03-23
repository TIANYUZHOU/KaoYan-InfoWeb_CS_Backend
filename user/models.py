from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    """自定义用户模型"""
    mobile = models.CharField('手机号', max_length=24, unique=True)
    avatar = models.ImageField('头像', upload_to='avatars/%Y/%m/%d', default='avatars/default.jpg')
    editTime = models.DateTimeField('编辑时间', auto_now=True)

    class Meta:
        # db_table = 'user_users'   # 数据库表名
        verbose_name = '用户'
        verbose_name_plural = '用户'
