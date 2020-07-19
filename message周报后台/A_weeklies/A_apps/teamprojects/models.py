from datetime import datetime

from django.db import models

from users.models import UserProfile


class Project(models.Model):
    """项目"""
    author = models.ForeignKey(UserProfile, verbose_name="作者", related_name='project', on_delete=models.CASCADE)
    name = models.CharField(max_length=60, verbose_name="名称")
    project_type = models.CharField(max_length=20, verbose_name="类型", null=True, blank=True)
    group_leader = models.CharField(max_length=15, verbose_name='负责人', null=True, blank=True)
    describe = models.TextField(max_length=1000, verbose_name="项目描述", null=True, blank=True)
    start_date = models.DateField(auto_now_add=True, verbose_name="开始日期")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "项目"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class ProjectMember(models.Model):
    """项目成员"""
    project = models.ForeignKey(Project, related_name='projectmembers', verbose_name="项目", on_delete=models.CASCADE)
    name = models.CharField(max_length=20, verbose_name="姓名")
    occupation = models.CharField(max_length=20, null=True, blank=True, verbose_name="职位")
    task = models.CharField(max_length=100, null=True, blank=True, verbose_name="任务")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "项目成员"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
