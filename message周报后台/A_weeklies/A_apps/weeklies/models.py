from datetime import datetime

from django.db import models

from users.models import UserProfile


class Weekly(models.Model):
    """周报"""
    author = models.ForeignKey(UserProfile, verbose_name="作者", related_name='weekly', on_delete=models.CASCADE)
    name = models.CharField(max_length=20, verbose_name="姓名")
    occupation = models.CharField(max_length=20, verbose_name="职位", null=True, blank=True)
    group_leader = models.CharField(max_length=20, verbose_name="组长", null=True, blank=True)
    plan = models.TextField(max_length=1000, verbose_name="任务计划", null=True, blank=True)
    completed = models.CharField(max_length=10, verbose_name="是否完成", null=True, blank=True)
    comment = models.CharField(max_length=150, verbose_name="管理员评论", null=True, blank=True)
    last_revision = models.DateField(auto_now=True, verbose_name="上次修改时间")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "周报"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s-%s" % (self.name, self.add_time)


class ProjectInWeekly(models.Model):
    """周报中填写的项目"""
    parentweekly = models.ForeignKey(Weekly, verbose_name="周报", related_name='weeklyprojects', on_delete=models.CASCADE)
    name = models.CharField(max_length=60, verbose_name="名称")
    project_type = models.CharField(max_length=20, verbose_name="类型", null=True, blank=True)
    time_plan = models.CharField(max_length=20, verbose_name="项目周期", null=True, blank=True)
    describe = models.TextField(max_length=500, verbose_name="项目描述", null=True, blank=True)
    status = models.CharField(max_length=20, verbose_name="项目状态", null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "周报中的项目"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
