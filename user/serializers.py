from rest_framework import serializers
from .models import User
from django.core.cache import cache


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

        password = validated_data.pop('password')  # password明文需要单独处理存储
        user = User(**validated_data)  # 创建Uer模型的对象给对应字段赋值
        user.set_password(password)  # 加密密码再赋值给user的password属性
        user.save() # 存储到数据库

        return user
