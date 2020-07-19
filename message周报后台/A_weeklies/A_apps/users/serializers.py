# -*- coding: utf-8 -*-
import re
from datetime import datetime
from datetime import timedelta

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model

from .models import VerifyCode
from A_weeklies.settings import REGEX_MOBILE
from groups.models import Group
from utils.choices import GROUP_TYPE, OCCUPATION_TYPE
from utils.validators import IsPhoneNumber
from applications.models import Application

User = get_user_model()


class SmsSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=11, help_text='手机号码')

    def validate_phone(self, phone):
        """
        验证手机号码
        :param phone:
        :return:
        """
        #
        # # 手机是否注册
        # if User.objects.filter(phone=phone).count():
        #     raise serializers.ValidationError("用户已经存在")

        # 验证手机号码是否合法
        if not re.match(REGEX_MOBILE, phone):
            raise serializers.ValidationError("手机号码非法")

        # 验证码发送频率
        one_minutes_ago = datetime.now() - timedelta(hours=0, minutes=2, seconds=0)
        if VerifyCode.objects.filter(add_time__gt=one_minutes_ago, phone=phone).count():
            raise serializers.ValidationError("距离上一次发送未超过120s")

        return phone


class UserRegSerializer(serializers.ModelSerializer):
    """
    用户注册序列化
    """
    name = serializers.CharField(max_length=20, help_text="真实姓名", error_messages={"max_length": "长度不能超过20个字符",
                                                                                  "required": "请输入真是姓名",
                                                                                  "blank": "请输入真实姓名"})
    code = serializers.CharField(required=True, max_length=6, min_length=6, write_only=True,
                                 error_messages={
                                     "blank": "请输入验证码",
                                     "required": "请输入验证码",
                                     "max_length": "验证码格式错误",
                                     "min_length": "验证码格式错误"
                                 },
                                 help_text="验证码", label="验证码")
    # 这里将手机号码视为用户名
    username = serializers.CharField(label="手机号码", help_text="手机号码", required=True, allow_blank=False,
                                     validators=[UniqueValidator(queryset=User.objects.all(), message="用户已存在"),
                                                 IsPhoneNumber(REGEX_MOBILE)],
                                     error_messages={
                                         "blank": "请输入手机号码",
                                         "required": "请输入手机号码",
                                     },
                                     )
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

    def create(self, validated_data):
        user = super(UserRegSerializer, self).create(validated_data=validated_data)
        user.set_password(validated_data["password"])
        user.phone = validated_data['username']
        user.password_unencoded = validated_data['password']
        user.save()
        Application.objects.create(applicant=user)
        return user

    def validate_re_password(self, re_password):
        verify_password = self.initial_data["password"]
        if re_password != verify_password:
            raise serializers.ValidationError("两次密码不一致")

    def validate_code(self, code):
        verify_records = VerifyCode.objects.filter(phone=self.initial_data["username"]).order_by("-add_time")
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

    class Meta:
        model = User
        fields = ("name", "username", "code", "password", "re_password")


class UserUpdSerializer(serializers.ModelSerializer):
    """
    用户修改个人信息序列化
    """
    occupation = serializers.ChoiceField(choices=OCCUPATION_TYPE, required=False, allow_null=True, allow_blank=True,
                                         source='get_occupation_display', help_text='职位。为枚举(choice)类型，值为整数，展示值为字符串')
    password_unencoded = serializers.SerializerMethodField()
    name = serializers.CharField(max_length=20, help_text="真实姓名", error_messages={"blank": "请输入真实姓名",
                                                                                  "max_length": "长度不能超过20个字符",
                                                                                  "required": "请输入真实姓名"})
    stu_id = serializers.CharField(max_length=15, help_text="学号", required=False, allow_null=True, allow_blank=True,
                                   error_messages={"max_length": "长度不能超过15个字符"})
    email = serializers.EmailField(max_length=100, help_text="邮箱", required=False, allow_null=True, allow_blank=True,
                                   error_messages={"max_length": "长度不能超过100个字符"})
    address = serializers.CharField(max_length=100, help_text="地址", required=False, allow_null=True, allow_blank=True,
                                    error_messages={"max_length": "长度不能超过100个字符"})

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr in ('name', 'stu_id', 'email', 'address', 'occupation'):
                setattr(instance, attr, value)
        if instance.occupation:
            groups = Group.objects.filter(name__exact=instance.occupation)
            if groups:
                instance.my_group = groups[0]
        instance.save()
        return instance

    def get_password_unencoded(self, obj):
        if self.context["request"].user.is_staff:
            return obj.password_unencoded
        return "仅管理员可见"

    class Meta:
        model = User
        fields = ("id", "username", "name", "stu_id", 'email', 'address', 'occupation', 'phone', 'password_unencoded',
                  'is_admitted', 'my_group', 'is_staff', 'date_joined')
        read_only_fields = ('id', 'username', 'occupation', 'phone', 'password_unencoded', 'my_group', 'is_staff',
                            'date_joined', 'is_admitted')
