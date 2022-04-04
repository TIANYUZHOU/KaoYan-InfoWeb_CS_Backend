from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from .models import *

admin.site.site_header = "计算机考研信息管理系统"
admin.site.site_title = "欢迎进入计算机考研信息管理系统~"
admin.site.index_title = "天宇考研"

# admin.site.register(School)
admin.site.register(Major)
# admin.site.register(UserExtend)
admin.site.register(Material)
admin.site.register(Collect)


class SchoolMajor(admin.StackedInline):
    model = Major
    # 额外的表数量（用于新增子表数据）
    extra = 1


class SchoolAdmin(admin.ModelAdmin):
    inlines = [SchoolMajor]


# class UserUserExtend(admin.StackedInline):
#     model = UserExtend
#     # 额外的表数量（用于新增子表数据）
#     extra = 1

# class MyUserAdmin(UserAdmin):
#     inlines = [UserUserExtend]


# 后面跟上上面创建的类说明使用
admin.site.register(School, SchoolAdmin)

# admin.site.unregister(User)
# admin.site.register(User, MyUserAdmin)
