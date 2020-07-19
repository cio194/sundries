from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import GroupSerializer
from .models import Group
from utils.permissions import IsAuthenticated1


class GroupViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
    返回组的列表页

    read:
    返回某一个组的详细信息
    """
    permission_classes = (IsAuthenticated1, )
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    authentication_classes = (SessionAuthentication, JSONWebTokenAuthentication)

