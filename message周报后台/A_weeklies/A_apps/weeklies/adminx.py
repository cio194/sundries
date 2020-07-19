# -*- coding: utf-8 -*-


import xadmin

from .models import Weekly, ProjectInWeekly


class WeeklyAdmin(object):
    list_display = ['author', 'group_leader', 'plan', 'completed', 'add_time']
    search_fields = ['author__name', 'author__stu_id', 'group_leader', 'plan', 'completed']
    list_filter = ['author__name', 'author__stu_id', 'group_leader', 'plan', 'completed', 'add_time']


class ProjectInWeeklyAdmin(object):
    list_display = ['name', 'time_plan', 'describe', 'status', 'add_time']
    search_fields = ['name', 'time_plan', 'describe', 'status']
    list_filter = ['name', 'time_plan', 'describe', 'status', 'add_time']


xadmin.site.register(Weekly, WeeklyAdmin)
xadmin.site.register(ProjectInWeekly, ProjectInWeeklyAdmin)