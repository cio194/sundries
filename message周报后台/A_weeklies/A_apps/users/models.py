from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

from groups.models import Group
from utils.choices import OCCUPATION_TYPE


class UserProfile(AbstractUser):
    """用户"""
    name = models.CharField(max_length=20, verbose_name="真实姓名")
    stu_id = models.CharField(max_length=15, null=True, blank=True, verbose_name="学号")
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="邮箱")
    address = models.CharField(max_length=100, null=True, blank=True, verbose_name="地址")
    occupation = models.IntegerField(choices=OCCUPATION_TYPE, null=True, blank=True, verbose_name="职位")
    phone = models.CharField(max_length=11, null=True, blank=True, verbose_name="电话")
    my_group = models.ForeignKey(Group, related_name='groupmembers', null=True, blank=True, verbose_name="所属组",
                                 on_delete=models.SET_NULL)
    password_unencoded = models.CharField(max_length=16, null=True, blank=True, verbose_name="管理员可见密码")
    is_admitted = models.BooleanField(default=False, verbose_name="是否申请成功")
    is_staff = models.BooleanField(default=False, verbose_name='是否为管理员', help_text="是否为管理员")

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.username


class VerifyCode(models.Model):
    """短信验证码"""
    code = models.CharField(max_length=10, verbose_name="验证码")
    phone = models.CharField(max_length=11, verbose_name="电话")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "短信验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code
