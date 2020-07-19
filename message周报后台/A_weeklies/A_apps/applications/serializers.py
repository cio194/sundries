# -*- coding: utf-8 -*-

from rest_framework import serializers

from .models import Application
from users.models import UserProfile


class ApplicantSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('id', 'name', 'phone')
        read_only_fields = fields


class ApplicationSerializer(serializers.ModelSerializer):
    applicant = ApplicantSerializer(read_only=True)
    resp = serializers.BooleanField(help_text='管理员处理申请，0为拒绝，1为同意', error_messages={"blank": "请选择同意或拒绝",
                                                                                   "required": "请选择同意或拒绝"})

    def save(self):
        if self.validated_data["resp"]:
            self.instance.applicant.is_admitted = True
            self.instance.applicant.save()
        else:
            self.instance.applicant.delete()
        self.instance.delete()

    class Meta:
        model = Application
        fields = ('id', 'applicant', 'resp', 'add_time')
        read_only_fields = ('id', 'applicant', 'add_time')
