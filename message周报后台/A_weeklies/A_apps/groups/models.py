from datetime import datetime

from django.db import models

from utils.choices import GROUP_TYPE


class Group(models.Model):
    """组"""
    name = models.IntegerField(choices=GROUP_TYPE, unique=True, verbose_name="名称")
    img = models.ImageField(upload_to="group_images/", null=True, blank=True, verbose_name="组的封面")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "组"
        verbose_name_plural = verbose_name

    def __str__(self):
        return GROUP_TYPE[self.name-1][1]

