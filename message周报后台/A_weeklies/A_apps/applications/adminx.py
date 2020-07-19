# -*- coding: utf-8 -*-
import xadmin

from .models import Application


class ApplicationAdmin(object):
    list_display = ['id', 'applicant', 'resp', 'add_time']


xadmin.site.register(Application, ApplicationAdmin)