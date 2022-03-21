from django.shortcuts import render
from rest_framework.response import Response

from rest_framework.views import APIView
from random import randint
from libs import send_messages

import logging

logger = logging.getLogger('django')


# Create your views here.

class SMSCodeView(APIView):
    """短信验证码"""

    def get(self, request, mobile):
        # 1. 生成验证码
        sms_code = '%06d' % randint(0, 999999)  # 前闭后闭，不够 6 位补 0
        logger.info(sms_code)
        # 2. 创建redis连接对象
        # 3. 把验证码存储到redis数据库
        # 4. 发短信验证码
        send_messages.SendMessage().SMS(mobile, sms_code)

        return Response({'code': '200'})
