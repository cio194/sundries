# -*- coding: utf-8 -*-


import xadmin

from .models import Project, ProjectMember


class ProjectAdmin(object):
    list_display = ['name', 'project_type', 'describe', 'start_date', 'add_time']
    search_fields = ['name', 'project_type']
    list_filter = ['name', 'project_type', 'describe', 'start_date', 'add_time']


class ProjectMemberAdmin(object):
    list_display = ['project', 'name', 'occupation', 'task', 'add_time']
    search_fields = ['project__name', 'name', 'occupation', 'task']
    list_filter = ['project__name', 'name', 'occupation', 'task', 'add_time']


xadmin.site.register(Project, ProjectAdmin)
xadmin.site.register(ProjectMember, ProjectMemberAdmin)