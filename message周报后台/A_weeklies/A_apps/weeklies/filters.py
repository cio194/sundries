# -*- coding: utf-8 -*-

import django_filters
from django.db.models import Q

from .models import Weekly


class WeeklyFilter(django_filters.rest_framework.FilterSet):
    """
    周报的过滤类
    """
    start_time = django_filters.DateTimeFilter(field_name='add_time', lookup_expr='date__gte')
    end_time = django_filters.DateTimeFilter(field_name='add_time', lookup_expr='date__lte')

    class Meta:
        model = Weekly
        fields = ['author', 'start_time', 'end_time']
