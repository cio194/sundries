from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import WeeklySerializer, WeeklyComSerializer
from .models import Weekly
from .filters import WeeklyFilter
from utils.permissions import IsOwnerOrReadOnly1, IsAuthenticated1


class WeekliesPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100


class WeekliesViewset(viewsets.ModelViewSet):
    """
    list:
    返回周报列表页，以添加时间排序

    create:
    创建周报

    read:
    返回某一周报的详细信息

    update:
    更新某一周报信息（仅能更新自己的周报）

    partial_update:
    更新评论（当用户为管理员时才能进行此操作，且管理员无法评论自己的周报，普通用户无法使用patch）

    delete:
    删除某一周报（仅能删除自己的周报）
    """
    permission_classes = (IsAuthenticated1, IsOwnerOrReadOnly1)
    queryset = Weekly.objects.all().order_by('add_time', )
    authentication_classes = (SessionAuthentication, JSONWebTokenAuthentication)
    pagination_class = WeekliesPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_class = WeeklyFilter
    search_fields = ('group_leader', 'plan')

    def get_serializer_class(self):
        if self.action == 'partial_update':
            return WeeklyComSerializer
        else:
            return WeeklySerializer
