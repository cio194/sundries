# -*- coding: utf-8 -*-

import django_filters

from .models import Project


class ProjectFilter(django_filters.rest_framework.FilterSet):
    """
    团队项目的过滤类
    """
    start_time = django_filters.DateTimeFilter(field_name='add_time', lookup_expr='date__gte')
    end_time = django_filters.DateTimeFilter(field_name='add_time', lookup_expr='date__lte')

    class Meta:
        model = Project
        fields = ['start_time', 'end_time']
