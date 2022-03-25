# 继承Django权限处理类后增加多种账号登录验证功能
from django.contrib.auth.backends import ModelBackend
from .models import User
import re
from django.core.cache import cache


def get_user_by_account(account):
    """通过传入的账户获取user模型对象
    :param account: 可以是手机号可以是用户名
    :return user或None
    """
    try:
        if re.match(r'^1[3-9]\d{9}$', account):
            user = User.objects.get(mobile=account)
        else:
            user = User.objects.get(username=account)
    except User.DoesNotExist:
        return None
    else:
        return user


class UserNameMobileAuthBackend(ModelBackend):
    """修改Django的认证类实现多账号登录"""

    def authenticate(self, request, username=None, password=None, **kwargs):
        # 获取user
        user = get_user_by_account(username)
        # 判断密码是否正确（用户名/手机号 + 密码登录）
        # username 为 username 或 mobile
        if user and user.check_password(password):
            return user
        # 判断验证码是否正确（手机号 + 验证码登录）
        # username 为 mobile
        # password 为 用户提交的验证码
        elif user and password == cache.get('sms_%s' % username):
            return user
