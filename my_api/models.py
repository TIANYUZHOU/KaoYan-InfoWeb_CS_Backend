from django.db import models
from django.contrib.auth.models import User

# Create your models here.

from django.db.models.signals import post_save
from django.dispatch import receiver


# 用户扩展表
class UserExtend(models.Model):
    # 关联上系统本身的User表 on_delete级联删除（关联的表中数据一起被删除）
    user = models.OneToOneField(User, related_name='extension', on_delete=models.CASCADE)
    phone = models.CharField('手机号', max_length=64, unique=True)
    avatar = models.ImageField('头像', upload_to='avatars/%Y/%m/%d',default='avatars/default.jpg')
    addTime = models.DateTimeField('添加时间', auto_now_add=True)
    editTime = models.DateTimeField('编辑时间', auto_now=True)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ['id']
        verbose_name = '用户扩展'
        verbose_name_plural = '用户扩展'


# 当接收到User表.save()运行的信号之后，执行下面函数
@receiver(post_save, sender=User)
# instance表示被保存的对象(实例)
# created 布尔值; True如果创建了新记录（True表示数据创建）
# 参考https://www.jb51.net/article/164598.htm
def create_user_extension(instance, created, **kwargs):
    if created:
        # 如果第一次创建userextension绑定
        UserExtend.objects.create(user=instance)
    else:
        # 修改user对象，那么也要将extension进行保存
        instance.extension.save()


# 院校表
class School(models.Model):
    schName = models.CharField('院校名称', max_length=255)
    location = models.CharField('所在地', max_length=255)
    subjection = models.CharField('院校隶属', max_length=255)
    graSchool = models.BooleanField('研究生院')
    indLine = models.BooleanField('自主划线')
    annUrl = models.TextField('网报公告')
    admGuideUrl = models.TextField('招生简章')
    adMethodUrl = models.TextField('调剂办法')

    def __str__(self):
        return self.schName

    class Meta:
        ordering = ['id']
        verbose_name = '院校表'
        verbose_name_plural = '院校表'


# 专业表
class Major(models.Model):
    school = models.ForeignKey('School', verbose_name='院校名称', on_delete=models.DO_NOTHING)
    major = models.CharField('专业', max_length=255)
    resDirection = models.CharField('研究方向', max_length=255)
    institute = models.CharField('院系所', max_length=255)
    enrPlan = models.CharField('招生计划', max_length=255)
    examForm = models.CharField('考试方式', max_length=8)
    learnForm = models.CharField('学习方式', max_length=12)
    examScope = models.TextField('考试范围')
    remark = models.TextField('备注')

    def __str__(self):
        return self.major

    class Meta:
        ordering = ['id']
        verbose_name = '专业表'
        verbose_name_plural = '专业表'


# 资料表
class Material(models.Model):
    matName = models.CharField('资料名称', max_length=255)
    file = models.FileField(upload_to='materials/%Y/%m/%d/')
    user = models.ForeignKey(User, verbose_name='上传用户',  on_delete=models.DO_NOTHING)
    school = models.ForeignKey('School', verbose_name='所属学校', null=True, on_delete=models.DO_NOTHING)
    uploadTime = models.DateTimeField('上传时间', auto_now_add=True)
    # downloadLink = models.TextField('下载链接')  DRF已封装好，不用自己取链接

    def __str__(self):
        return self.matName

    class Meta:
        ordering = ['id']
        verbose_name = '资料表'
        verbose_name_plural = '资料表'
