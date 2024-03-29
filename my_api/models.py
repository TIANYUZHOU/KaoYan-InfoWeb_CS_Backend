from django.db import models
# from django.contrib.auth.models import User
from user.models import User

# Create your models here.

from django.db.models.signals import post_save
from django.dispatch import receiver


# 用户扩展表
# class UserExtend(models.Model):
#     # 关联上系统本身的User表 on_delete级联删除（关联的表中数据一起被删除）
#     user = models.OneToOneField(User, related_name='extension', on_delete=models.CASCADE)
#     phone = models.CharField('手机号', max_length=64, unique=True)
#     avatar = models.ImageField('头像', upload_to='avatars/%Y/%m/%d', default='avatars/default.jpg')
#     addTime = models.DateTimeField('添加时间', auto_now_add=True)
#     editTime = models.DateTimeField('编辑时间', auto_now=True)
#
#     def __str__(self):
#         return self.user.username
#
#     class Meta:
#         ordering = ['id']
#         verbose_name = '用户扩展表'
#         verbose_name_plural = '用户扩展表'


# # 当接收到User表.save()运行的信号之后，执行下面函数
# @receiver(post_save, sender=User)
# # instance表示被保存的对象(实例)
# # created 布尔值; True如果创建了新记录（True表示数据创建）
# # 参考https://www.jb51.net/article/164598.htm
# def create_user_extension(instance, created, **kwargs):
#     if created:
#         # 如果第一次创建userextension绑定
#         UserExtend.objects.create(user=instance)
#     else:
#         # 修改user对象，那么也要将extension进行保存
#         instance.extension.save()


# 院校表
class School(models.Model):
    schName = models.CharField('院校名称', max_length=255)
    location = models.CharField('所在地', max_length=255)
    subjection = models.CharField('院校隶属', max_length=255)
    is_985 = models.BooleanField('985工程', default=False)
    is_211 = models.BooleanField('211工程', default=False)
    is_firClassU = models.BooleanField('一流大学', default=False)
    is_firClassS = models.BooleanField('一流学科', default=False)
    is_else = models.BooleanField('四非', default=False)
    assessmentCS = models.CharField('计算机学科评估', max_length=8, null=True, blank=True, default='')
    assessmentSE = models.CharField('软件学科评估', max_length=8, null=True, blank=True, default='')
    graSchool = models.BooleanField('研究生院', default=False)
    indLine = models.BooleanField('自主划线', default=False)
    annUrl = models.TextField('网报公告', null=True, blank=True, default='')
    admGuideUrl = models.TextField('招生简章', null=True, blank=True, default='')
    adMethodUrl = models.TextField('调剂办法', null=True, blank=True, default='')
    proCourseCount = models.CharField('专业课考试门数', max_length=18, default='四零八')

    def __str__(self):
        return self.schName

    class Meta:
        ordering = ['id']
        verbose_name = '院校'
        verbose_name_plural = '院校'


# 专业表
class Major(models.Model):
    school = models.ForeignKey('School', verbose_name='院校名称', on_delete=models.DO_NOTHING)
    major = models.CharField('专业', max_length=255)
    resDirection = models.CharField('研究方向', max_length=255)
    institute = models.CharField('院系所', max_length=255)
    admScore = models.CharField('复试分数', blank=True, null=True, max_length=255)
    # institute = models.ForeignKey('Institute',verbose_name='院系所',on_delete=models.DO_NOTHING)
    enrPlan = models.CharField('招生计划', max_length=255)
    examForm = models.CharField('考试方式', max_length=8)
    learnForm = models.CharField('学习方式', max_length=12)
    examScope = models.TextField('考试范围')
    remark = models.TextField('备注', null=True, blank=True, default='')

    def __str__(self):
        return self.major

    class Meta:
        ordering = ['id']
        verbose_name = '专业'
        verbose_name_plural = '专业'


# 资料表
class Material(models.Model):
    MATH = 'MATH'
    ENGLISH = 'EN'
    POLITICS = 'POL'
    PUBLIC_COURSE_COMBINATION = 'PUCC'
    FZE = '408'
    DATA_STRUCTURE = 'DS'
    OPERATING_SYSTEM = 'OS'
    COMPUTER_NETWORK = 'CN'
    COMPUTER_ORGANIZATION = 'CO'
    PROFESSIONAL_COURSE_COMBINATION = 'PRCC'
    ELSE = 'ELSE'
    CLASSIFICATION_IN_MATERIAL_CHOICES = [
        (MATH, '数学'),
        (ENGLISH, '英语'),
        (POLITICS, '政治'),
        (PUBLIC_COURSE_COMBINATION, '公共课资料'),
        (FZE, '408'),
        (DATA_STRUCTURE, '数据结构'),
        (OPERATING_SYSTEM, '操作系统'),
        (COMPUTER_NETWORK, '计算机网络'),
        (COMPUTER_ORGANIZATION, '计算机组成原理'),
        (PROFESSIONAL_COURSE_COMBINATION, '专业课资料'),
        (ELSE, '其他'),
    ]

    matName = models.CharField('资料名称', max_length=255)
    file = models.FileField('文件', upload_to='materials/%Y/%m/%d/')
    fileSize = models.CharField('文件大小', max_length=255, blank=True, null=True)
    user = models.ForeignKey(User, verbose_name='上传用户', on_delete=models.DO_NOTHING, related_name='matUser')
    downloads = models.IntegerField('下载量', default=0)
    school = models.ForeignKey('School', verbose_name='所属学校', null=True, on_delete=models.DO_NOTHING,
                               related_name='matSchool')
    uploadTime = models.DateTimeField('上传时间', auto_now_add=True)
    matClass = models.CharField('资料分类', max_length=8, choices=CLASSIFICATION_IN_MATERIAL_CHOICES, default=ELSE)
    description = models.TextField('资料描述', default='快下载来看看~')

    # downloadLink = models.TextField('下载链接')  DRF已封装好，不用自己取链接

    def __str__(self):
        return self.matName

    class Meta:
        ordering = ['id']
        verbose_name = '资料'
        verbose_name_plural = '资料'


# 友情链接表
class Link(models.Model):
    webTitle = models.CharField('网站标题', max_length=24)
    url = models.CharField('网址', max_length=255)
    intro = models.TextField('网站简介', null=True, blank=True)

    def __str__(self):
        return self.webTitle

    class Meta:
        ordering = ['id']
        verbose_name = '友链'
        verbose_name_plural = '友链'


class Collect(models.Model):
    user = models.OneToOneField(User, verbose_name='收藏用户', on_delete=models.DO_NOTHING, related_name='colUser')
    school = models.ManyToManyField('School', blank=True, verbose_name='院校名称', related_name='colSchool')

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ['id']
        verbose_name = '收藏'
        verbose_name_plural = '收藏'


# 二级学院表
# class Institute(models.Model):
#     insName = models.CharField('院系所', max_length=255)
#     MATH1 = 'MATH1'
#     MATH2 = 'MATH2'
#     MATH3 = 'MATH3'
#     ENGLISH1 = 'EN1'
#     ENGLISH2 = 'EN2'
#     PRO_COURSE_COUNT1 = '1'
#     PRO_COURSE_COUNT2 = '2'
#     PRO_COURSE_COUNT3 = '3'
#     PRO_COURSE_COUNT4 = '4'
#     PRO_COURSE_COUNT5 = '408'
#     SUBJECT_IN_MATH_CHOICES = [
#         (MATH1, '数学一'),
#         (MATH2, '数学二'),
#         (MATH3, '数学三')
#     ]
#     SUBJECT_IN_ENGLISH_CHOICES = [
#         (ENGLISH1, '英语一'),
#         (ENGLISH2, '英语二'),
#     ]
#     SUBJECT_IN_PRO_COURSE_COUNT_CHOICES = [
#         (PRO_COURSE_COUNT1, '1门'),
#         (PRO_COURSE_COUNT2, '2门'),
#         (PRO_COURSE_COUNT3, '3门'),
#         (PRO_COURSE_COUNT4, '4门')
#     ]
#     school = models.ForeignKey('School', verbose_name='所属学校', null=True, on_delete=models.DO_NOTHING,
#                                related_name='secSchool')
#     math = models.CharField('数学', max_length=8, default=MATH1)
#     english = models.CharField('英语科目选择', max_length=8, choices=SUBJECT_IN_ENGLISH_CHOICES, default=ENGLISH1)
#     proCourseCount = models.CharField('专业课科目选择', max_length=8, choices=SUBJECT_IN_PRO_COURSE_COUNT_CHOICES,
#                                       default=PRO_COURSE_COUNT5)


class Feedback(models.Model):
    user = models.ForeignKey(User, verbose_name='反馈用户', on_delete=models.CASCADE, related_name='feedUser')
    content = models.TextField('反馈内容', null=True, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ['id']
        verbose_name = '反馈'
        verbose_name_plural = '反馈'
