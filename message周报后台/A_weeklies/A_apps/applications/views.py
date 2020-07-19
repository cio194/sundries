from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework import mixins
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Application
from .serializers import ApplicationSerializer
from utils.permissions import IsAuthenticated1


class ApplicationsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100


class ApplicationViewset(mixins.UpdateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    list:
    返回申请列表页，以添加时间排序

    partial_update:
    接受resp，之后删除相应申请，并对相关user进行处理（删除或者修改is_admitted字段，put和patch效果相同)
    """
    queryset = Application.objects.all().order_by('add_time')
    serializer_class = ApplicationSerializer
    pagination_class = ApplicationsPagination
    permission_classes = (IsAdminUser, IsAuthenticated1)
    authentication_classes = (SessionAuthentication, JSONWebTokenAuthentication)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)
