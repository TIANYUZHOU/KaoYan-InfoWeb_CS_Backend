# Generated by Django 4.0.3 on 2022-03-18 14:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schName', models.CharField(max_length=255, verbose_name='院校名称')),
                ('location', models.CharField(max_length=255, verbose_name='所在地')),
                ('subjection', models.CharField(max_length=255, verbose_name='院校隶属')),
                ('graSchool', models.IntegerField(max_length=8, verbose_name='研究生院')),
                ('indLine', models.IntegerField(max_length=8, verbose_name='自主划线')),
                ('annUrl', models.TextField(verbose_name='网报公告')),
                ('admGuideUrl', models.TextField(verbose_name='招生简章')),
                ('adMethodUrl', models.TextField(verbose_name='调剂办法')),
            ],
            options={
                'verbose_name': '院校表',
                'verbose_name_plural': '院校表',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='UserExtend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=64, unique=True, verbose_name='手机号')),
                ('iconImage', models.ImageField(blank=True, null=True, upload_to='icon_img/%Y/%m/%d/', verbose_name='头像')),
                ('addTime', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('editTime', models.DateTimeField(auto_now=True, verbose_name='编辑时间')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='extension', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '注册用户',
                'verbose_name_plural': '注册用户',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('majoy', models.CharField(max_length=255, verbose_name='专业')),
                ('resDirection', models.CharField(max_length=255, verbose_name='研究方向')),
                ('institute', models.CharField(max_length=255, verbose_name='院系所')),
                ('enrPlan', models.CharField(max_length=255, verbose_name='招生计划')),
                ('examForm', models.CharField(max_length=8, verbose_name='考试方式')),
                ('learnForm', models.CharField(max_length=12, verbose_name='学习方式')),
                ('examScope', models.TextField(verbose_name='考试范围')),
                ('remark', models.TextField(verbose_name='备注')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='my_api.school', verbose_name='院校名称')),
            ],
            options={
                'verbose_name': '专业表',
                'verbose_name_plural': '专业表',
                'ordering': ['id'],
            },
        ),
    ]
