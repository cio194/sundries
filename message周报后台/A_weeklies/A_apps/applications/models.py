from datetime import datetime

from django.db import models

from users.models import UserProfile


class Application(models.Model):
    """
    申请
    """
    applicant = models.OneToOneField(UserProfile, related_name='application', on_delete=models.CASCADE)
    resp = models.BooleanField(default=False, verbose_name="管理员申请处理")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "申请"
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.applicant.name:
            return self.applicant.name
        else:
            return self.applicant.username
