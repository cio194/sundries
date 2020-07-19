# -*- coding: utf-8 -*-
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .serializers import ForgetSerializer
from users.models import UserProfile


class ForgetViewset(viewsets.GenericViewSet):
    """
    partial_update:
    修改密码
    """
    queryset = UserProfile.objects.all()
    serializer_class = ForgetSerializer
    authentication_classes = ()

    def partial_update(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
