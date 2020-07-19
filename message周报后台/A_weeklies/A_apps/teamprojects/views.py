from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import ProjectSerializer
from .models import Project
from .filters import ProjectFilter
from utils.permissions import IsAuthenticated1, IsOwnerOrReadOnly3


class ProjectPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100


class ProjectViewset(viewsets.ModelViewSet):
    """
    list:
    返回团队项目列表页，以添加时间排序

    create:
    创建团队项目

    read:
    返回某一项目详细信息

    update:
    更新某一项目（只能更新自己创建的项目）

    delete:
    删除某一项目（只能删除自己创建的项目）
    """
    permission_classes = (IsAuthenticated1, IsOwnerOrReadOnly3)
    queryset = Project.objects.all().order_by('add_time', )
    serializer_class = ProjectSerializer
    authentication_classes = (SessionAuthentication, JSONWebTokenAuthentication)
    pagination_class = ProjectPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_class = ProjectFilter
    search_fields = ('group_leader', 'name', 'describe')
