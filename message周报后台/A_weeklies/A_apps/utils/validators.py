# -*- coding: utf-8 -*-
import re

from rest_framework import serializers

from users.models import UserProfile


class IsPhoneNumber(object):
    def __init__(self, style):
        self.style = style

    def __call__(self, value):
        if not re.match(self.style, value):
            raise serializers.ValidationError("手机号码非法")


class UserExist(object):
    def __call__(self, value):
        if not UserProfile.objects.filter(phone__exact=value):
            raise serializers.ValidationError('用户不存在')
