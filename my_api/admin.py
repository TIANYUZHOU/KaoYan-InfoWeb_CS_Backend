from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from .models import *

admin.site.site_header = "『上岸吧』管理系统"
admin.site.site_title = "欢迎进入『上岸吧』管理系统~"
admin.site.index_title = "上岸吧"

# admin.site.register(School)
# admin.site.register(Major)
# admin.site.register(UserExtend)
admin.site.register(Material)
admin.site.register(Collect)
admin.site.register(Link)
admin.site.register(Feedback)


# class SchoolMajor(admin.StackedInline):
#     model = Major
#     # 额外的表数量（用于新增子表数据）
#     extra = 1
#
#
# class SchoolAdmin(admin.ModelAdmin):
#     inlines = [SchoolMajor]


# class UserUserExtend(admin.StackedInline):
#     model = UserExtend
#     # 额外的表数量（用于新增子表数据）
#     extra = 1

# class MyUserAdmin(UserAdmin):
#     inlines = [UserUserExtend]


# 后面跟上上面创建的类说明使用
# admin.site.register(School, SchoolAdmin)


# admin.site.unregister(User)
# admin.site.register(User, MyUserAdmin)


class MajorAdmin(admin.ModelAdmin):
    # 需要显示的字段信息
    list_display = ('id', 'school', 'major', 'resDirection', 'institute')
    search_fields = ('school__schName', 'major', 'institute')
    # 设置哪些字段可以点击进入编辑界面，默认是第一个字段
    list_display_links = ('id', 'major')


admin.site.register(Major, MajorAdmin)


class SchoolAdmin(admin.ModelAdmin):
    list_display = ('id', 'schName', 'location', 'subjection', 'is_985', 'is_211',
                    'is_firClassU', 'is_firClassS', 'assessmentCS', 'assessmentSE')

    list_display_links = ('id', 'schName')
    search_fields = ('schName', 'location',)
    list_per_page = 10  # 定义一页为10条数据


admin.site.register(School, SchoolAdmin)
