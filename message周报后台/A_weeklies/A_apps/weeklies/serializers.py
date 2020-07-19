# -*- coding: utf-8 -*-


from rest_framework import serializers

from .models import Weekly, ProjectInWeekly


class ProjectInWeeklySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=60, help_text="名称", error_messages={"max_length": "长度不能超过60个字符",
                                                                                "required": "请输入项目名称",
                                                                                "blank": "请输入项目名称"})
    project_type = serializers.CharField(max_length=20, help_text="类型", required=False, allow_null=True, allow_blank=True,
                                         error_messages={"max_length": "长度不能超过20个字符"})
    time_plan = serializers.CharField(max_length=20, help_text="项目周期", required=False, allow_null=True, allow_blank=True,
                                      error_messages={"max_length": "长度不能超过20个字符"})
    describe = serializers.CharField(max_length=500, help_text="项目描述", required=False, allow_null=True, allow_blank=True,
                                     error_messages={"max_length": "长度不能超过500个字符"})
    status = serializers.CharField(max_length=20, help_text="项目状态", required=False, allow_null=True, allow_blank=True,
                                   error_messages={"max_length": "长度不能超过20个字符"})

    class Meta:
        model = ProjectInWeekly
        fields = '__all__'
        read_only_fields = ('id', 'add_time', 'parentweekly')


class WeeklySerializer(serializers.ModelSerializer):
    weeklyprojects = ProjectInWeeklySerializer(required=False, many=True, allow_null=True,
    help_text="周报内项目.嵌套字段，允许多个，字段有五个：name, project_type, time_plan, describe, status. 都是字符类型，仅name为required")
    name = serializers.CharField(max_length=20, help_text="姓名", error_messages={"max_length": "长度不能超过20个字符",
                                                                                "blank": "请输入姓名",
                                                                                "required": "请输入姓名"})
    occupation = serializers.CharField(max_length=20, allow_blank=True, allow_null=True, help_text="职位", required=False,
                                       error_messages={"max_length": "长度不能超过20个字符"})
    group_leader = serializers.CharField(max_length=20, help_text="组长", required=False, allow_blank=True, allow_null=True,
                                         error_messages={"max_length": "长度不能超过20个字符"})
    plan = serializers.CharField(max_length=1000, help_text="任务计划", required=False, allow_blank=True, allow_null=True,
                                 error_messages={"max_length": "长度不能超过1000个字符"})
    completed = serializers.CharField(max_length=10, help_text="是否完成", required=False, allow_blank=True, allow_null=True,
                                      error_messages={"max_length": "长度不能超过10个字符"})

    def create(self, validated_data):
        try:
            projects_data = validated_data.pop('weeklyprojects')
        except:
            projects_data = None
        weekly = Weekly.objects.create(author=self.context["request"].user, **validated_data)
        weekly.comment = ""
        if projects_data:
            for project_data in projects_data:
                ProjectInWeekly.objects.create(parentweekly=weekly, **project_data)
        return weekly

    def update(self, instance, validated_data):
        projects_instance = instance.weeklyprojects.all()
        if projects_instance:
            for project in projects_instance:
                project.delete()
        try:
            projects_data = validated_data.pop('weeklyprojects')
        except:
            projects_data = None
        if projects_data:
            for project_data in projects_data:
                ProjectInWeekly.objects.create(parentweekly=instance, **project_data)
        for attr, value in validated_data.items():
            if attr in ('name', 'occupation', 'group_leader', 'plan', 'completed'):
                setattr(instance, attr, value)
        instance.save()
        return instance

    class Meta:
        model = Weekly
        fields = "__all__"
        read_only_fields = ('id', 'author', 'last_revision', 'add_time', 'comment')


class WeeklyComSerializer(serializers.ModelSerializer):
    comment = serializers.CharField(max_length=150, help_text="评论", error_messages={"max_length": "长度不能超过150个字符",
                                                                                    "blank": "请填写评论",
                                                                                    "required": "请填写评论"})

    def update(self, instance, validated_data):
        if self.context["request"].user.is_staff:
            try:
                instance.comment = validated_data['comment']
            except:
                return instance
            instance.save()
        return instance

    class Meta:
        model = Weekly
        fields = ('comment', )
