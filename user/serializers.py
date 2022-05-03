from rest_framework import serializers

from my_api.serializers import MaterialInfoSerializer, InfoCollectSerializer
from .models import User
from my_api.models import Collect
from django.core.cache import cache
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CreateUserSerializer(serializers.ModelSerializer):
    """注册序列化器"""

    # 序列化器需要的所有字段
    # ['id','username','password','mobile','sms_code']
    # 序列化器需要校验的字段
    # ['username','password','mobile','sms_code']
    # 模型中已存在
    # ['id','username','password','mobile']

    # 需要序列化得到字段 ['id','username', 'mobile']
    # 需要反序列化的字段 ['username','password','mobile','sms_code']

    # 模型中不存在的字段
    sms_code = serializers.CharField(label='验证码', write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'mobile', 'sms_code']
        extra_kwargs = {  # 修改字段选项
            'password': {
                'write_only': True  # 只进行反序列化
            }
        }

    def validate(self, attrs):
        """校验验证码"""
        mobile = attrs['mobile']
        real_sms_code = cache.get('sms_%s' % mobile)
        if real_sms_code is None or attrs['sms_code'] != real_sms_code:
            raise serializers.ValidationError('验证码错误')
        return attrs

    # 重写create方法
    def create(self, validated_data):
        del validated_data['sms_code']  # sms_code 不需要存储到数据库

        # print(validated_data)
        password = validated_data.pop('password')  # password明文需要单独处理存储
        user = User(**validated_data)  # 创建Uer模型的对象给对应字段赋值
        user.set_password(password)  # 加密密码再赋值给user的password属性
        user.save()  # 存储到数据库

        # 同时为用户创建收藏夹
        user_obj = User.objects.get(username=validated_data['username'])
        print(user_obj)
        user_id = user_obj.id
        collect = Collect(user_id=user_id)
        collect.save()

        return user


# 如果自定义了用户表，那么就要使用这个方法来获取用户模型
# 没有自定义的话可以使用以下方式加载用户模型:
# from django.contrib.auth.models import User
# 不过这种是万能的
# User = get_user_model()


# 重写TokenObtainPairSerializer类的部分方法以实现自定义数据响应结构和payload内容
class MyTokenSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        """
        此方法往token的有效负载 payload 里面添加数据
        例如自定义了用户表结构，可以在这里面添加用户邮箱，头像图片地址，性别，年龄等可以公开的信息
        这部分放在token里面是可以被解析的，所以不要放比较私密的信息

        :param user: 用戶信息
        :return: token
        """
        token = super().get_token(user)
        # 添加个人信息
        # token['username'] = user.username
        return token

    def validate(self, attrs):
        """
        此方法为响应数据结构处理
        原有的响应数据结构无法满足需求，在这里重写结构如下：
        {
            "refresh": "xxxx.xxxxx.xxxxx",
            "access": "xxxx.xxxx.xxxx",
            "expire": Token有效期截止时间,
            "username": "用户名",
            "email": "邮箱"
        }

        :param attrs: 請求參數
        :return: 响应数据
        """
        # data是个字典
        # 其结构为：{'refresh': '用于刷新token的令牌', 'access': '用于身份验证的Token值'}
        data = super().validate(attrs)
        data['user_id'] = self.user.id
        data['username'] = self.user.username
        data['avatar'] = 'http://127.0.0.1:8000/media/' + str(self.user.avatar)
        # 查询出收藏夹id
        collect_obj = Collect.objects.get(user=self.user)
        data['colId'] = collect_obj.id
        # 查询用户收藏的学校id
        schIdList = []
        for item in collect_obj.school.all():
            schIdList.append(item.id)
        data['schIdList'] = schIdList
        return data


# 用户信息序列化器
class UsersProfileSerializer(serializers.ModelSerializer):
    matUser = MaterialInfoSerializer(many=True)
    colUser = InfoCollectSerializer(read_only=True)

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {  # 修改字段选项
            'password': {
                'write_only': True  # 只进行反序列化
            }
        }


# 修改用户信息序列化器
class UserInfoModifySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'mobile', 'avatar', 'signature']
