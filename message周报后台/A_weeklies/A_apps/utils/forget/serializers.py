# -*- coding: utf-8 -*-
from datetime import datetime
from datetime import timedelta

from rest_framework import serializers

from users.models import UserProfile, VerifyCode
from utils.validators import IsPhoneNumber, UserExist
from A_weeklies.settings import REGEX_MOBILE


class ForgetSerializer(serializers.Serializer):
    phone = serializers.CharField(label="手机号码", help_text="手机号码", allow_blank=False,
                                  validators=[IsPhoneNumber(REGEX_MOBILE), UserExist()],
                                  error_messages={
                                    "blank": "请输入手机号码",
                                    "required": "请输入手机号码",
                                  },)
    code = serializers.CharField(required=True, max_length=6, min_length=6, write_only=True,
                                 error_messages={
                                     "blank": "请输入验证码",
                                     "required": "请输入验证码",
                                     "max_length": "验证码格式错误",
                                     "min_length": "验证码格式错误"
                                 },
                                 help_text="验证码", label="验证码")
    password = serializers.CharField(
        style={'input_type': 'password'}, help_text="密码", label="密码", write_only=True, max_length=16, min_length=8,
        error_messages={
            "blank": "请输入密码",
            "required": "请输入密码",
            "max_length": "长度不能超过16个字符",
            "min_length": "长度不能少于8个字符"
        }
    )
    re_password = serializers.CharField(
        style={'input_type': 'password'}, help_text="确认密码", label="确认密码", write_only=True,
        error_messages={
            "blank": "请重复密码",
            "required": "请重复密码",
        }
    )

    def save(self, **kwargs):
        user = UserProfile.objects.filter(phone__exact=self.validated_data['phone'])[0]
        user.set_password(self.validated_data["password"])
        user.password_unencoded = self.validated_data['password']
        user.save()
        return user

    def validate_re_password(self, re_password):
        verify_password = self.initial_data["password"]
        if re_password != verify_password:
            raise serializers.ValidationError("两次密码不一致")

    def validate_code(self, code):
        verify_records = VerifyCode.objects.filter(phone=self.initial_data["phone"]).order_by("-add_time")
        if verify_records:
            last_record = verify_records[0]

            tow_minutes_ago = datetime.now() - timedelta(hours=0, minutes=2, seconds=0)
            if tow_minutes_ago > last_record.add_time:
                raise serializers.ValidationError("验证码过期")

            if last_record.code != code:
                raise serializers.ValidationError("验证码错误")

        else:
            raise serializers.ValidationError("验证码错误")

    def validate(self, attrs):
        del attrs["code"]
        del attrs["re_password"]
        return attrs