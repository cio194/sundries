# -*- coding: utf-8 -*-


import xadmin
from xadmin import views

from .models import VerifyCode


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "Spark Weeklies"
    site_footer = "Spark"
    menu_style = "accordion"


class VerifyCodeAdmin(object):
    list_display = ['code', 'phone', 'add_time']


xadmin.site.register(VerifyCode, VerifyCodeAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)