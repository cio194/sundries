from random import choice

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import SmsSerializer, UserRegSerializer, UserUpdSerializer
from utils.Sms import YunPian
from A_weeklies.settings import APIKEY
from .models import VerifyCode
from utils.permissions import IsAuthenticated2, IsOwnerOrReadOnly2

User = get_user_model()


class UsersPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100


class CustomBackend(ModelBackend):
    """
    自定义用户验证
    """
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username)|Q(phone=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class SmsCodeViewset(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    发送短信验证码
    """
    serializer_class = SmsSerializer
    authentication_classes = ()

    def generate_code(self):
        """
        生成四位数字的验证码
        :return:
        """
        seeds = "1234567890"
        random_str = []
        for i in range(6):
            random_str.append(choice(seeds))

        return "".join(random_str)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        phone = serializer.validated_data["phone"]

        yun_pian = YunPian(APIKEY)

        code = self.generate_code()

        sms_status = yun_pian.send_sms(code=code, phone=phone)

        if sms_status["code"] != 0:
            return Response({
                "phone": sms_status["msg"]
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            code_record = VerifyCode(code=code, phone=phone)
            code_record.save()
            return Response({
                "phone": phone
            }, status=status.HTTP_201_CREATED)


class UserViewset(viewsets.ModelViewSet):
    """
    list:
    返回用户列表页，以加入时间排序

    create:
    创建一个用户，已登录状态下不能访问，如果访问请进行重定向

    read:
    返回某一用户详细信息

    partial_update:
    更新用户个人信息（仅能更新自己的信息）(put和patch效果相同)

    delete:
    删除某一用户（仅管理员能删除用户，且管理员不能删除自己）
    """
    permission_classes = (IsAuthenticated2, IsOwnerOrReadOnly2)
    authentication_classes = (SessionAuthentication, JSONWebTokenAuthentication)
    queryset = User.objects.all().order_by('date_joined')
    pagination_class = UsersPagination

    def get_serializer_class(self):
        if self.action == 'create':
            self.authentication_classes = ()
            return UserRegSerializer
        return UserUpdSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)

        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict["token"] = jwt_encode_handler(payload)

        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()

