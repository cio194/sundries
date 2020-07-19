# -*- coding: utf-8 -*-

from rest_framework import serializers

from .models import Project, ProjectMember


class ProjectMemberSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=20, help_text="姓名", error_messages={"blank": "请输入姓名",
                                                                                "max_length": "长度不能超过20个字符",
                                                                                "required": "请输入姓名"})
    occupation = serializers.CharField(max_length=20, allow_blank=True, allow_null=True, help_text="职位", required=False,
                                       error_messages={"max_length": "长度不能超过20个字符"})
    task = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, help_text="任务", required=False,
                                 error_messages={"max_length": "长度不能超过100个字符"})

    class Meta:
        model = ProjectMember
        fields = '__all__'
        read_only_fields = ('id', 'add_time', 'project')


class ProjectSerializer(serializers.ModelSerializer):
    projectmembers = ProjectMemberSerializer(many=True,
                    help_text="组内成员.嵌套字段，允许多个，字段有三个：name, occupation, task. 都是字符类型，仅name为required")
    name = serializers.CharField(max_length=60, help_text="名称", error_messages={"blank": "请输入名称",
                                                                                "max_length": "长度不能超过60个字符",
                                                                                "required": "请输入名称"})
    project_type = serializers.CharField(max_length=20, help_text="项目类型", required=False, allow_blank=True, allow_null=True,
                                         error_messages={"max_length": "长度不能超过20个字符"})
    group_leader = serializers.CharField(max_length=15, help_text="负责人", required=False, allow_blank=True, allow_null=True,
                                         error_messages={"max_length": "长度不能超过20个字符"})
    describe = serializers.CharField(max_length=1000, help_text="项目描述", required=False, allow_blank=True, allow_null=True,
                                     error_messages={"max_length": "长度不能超过1000个字符"})

    def validate_projectmembers(self, projectmembers):
        try:
            if not projectmembers:
                raise serializers.ValidationError('至少需要一位成员')
        except:
            raise serializers.ValidationError('至少需要一位成员')

    def create(self, validated_data):
        projectmembers_data = validated_data.pop('projectmembers')
        project = Project.objects.create(author=self.context["request"].user, **validated_data)
        if projectmembers_data:
            for projectmember_data in projectmembers_data:
                ProjectMember.objects.create(project=project, **projectmember_data)
        return project

    def update(self, instance, validated_data):
        projectmembers_instance = instance.projectmembers.all()
        if projectmembers_instance:
            for projectmember in projectmembers_instance:
                projectmember.delete()
        projectmembers_data = validated_data.pop('projectmembers')
        if projectmembers_data:
            for projectmember_data in projectmembers_data:
                ProjectMember.objects.create(project=instance, **projectmember_data)
        for attr, value in validated_data.items():
            if attr in ('name', 'project_type', 'group_leader', 'describe'):
                setattr(instance, attr, value)
        instance.save()
        return instance

    class Meta:
        model = Project
        fields = "__all__"
        read_only_fields = ('id', 'author', 'add_time', 'start_time')
