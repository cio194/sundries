# -*- coding: utf-8 -*-


import xadmin

from .models import Group


class GroupAdmin(object):
    list_display = ['name', 'add_time']


xadmin.site.register(Group, GroupAdmin)