from django.contrib import admin

# Register your models here.

from .models import User


class UserAdmin(admin.ModelAdmin):
    # 需要显示的字段信息
    list_display = ('id', 'username', 'mobile', 'email', 'date_joined', 'editTime')

    # 设置哪些字段可以点击进入编辑界面，默认是第一个字段
    list_display_links = ('id', 'username')


admin.site.register(User, UserAdmin)
