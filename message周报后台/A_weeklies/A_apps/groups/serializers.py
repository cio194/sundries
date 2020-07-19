# -*- coding: utf-8 -*-

from rest_framework import serializers

from .models import Group
from users.models import UserProfile
from utils.choices import GROUP_TYPE, OCCUPATION_TYPE


class GroupMemberSerializer(serializers.ModelSerializer):
    occupation = serializers.ChoiceField(choices=OCCUPATION_TYPE, allow_null=True, allow_blank=True, source='get_occupation_display',
                                         help_text='职位。为枚举(choice)类型，值为整数，展示值为字符串')
    name = serializers.CharField(max_length=20, help_text="真实姓名", error_messages={"blank": "请选择同意或拒绝",
                                                                                  "max_length": "长度不能超过20个字符",
                                                                                  "required": "请选择同意或拒绝"})

    class Meta:
        model = UserProfile
        fields = ('id', 'name', 'occupation')


class GroupSerializer(serializers.ModelSerializer):
    groupmembers = GroupMemberSerializer(many=True)
    name = serializers.ChoiceField(choices=GROUP_TYPE, allow_null=True, allow_blank=True, source='get_name_display')

    class Meta:
        model = Group
        fields = '__all__'
