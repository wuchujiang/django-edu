import random

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler

from users.models import VerifyCode
from users.serializers import SmsSerializer, UserRegSerializer, UserDetailSerializer

User = get_user_model()


class CustomBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.object.get(Q(username=username) | Q(mobile=username))
            if user.check_password(password):
                return user

        except Exception as e:
            print(e, 'eee')
            return None


class SmsCodeViewset(CreateModelMixin, GenericViewSet):
    serializer_class = SmsSerializer

    # 随机生成4位验证码
    def generate_code(self):
        seeds = "1234567890"
        random_str = []
        for i in range(4):
            random_str.append(random.choice(seeds))

        return "".join(random_str)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        mobile = serializer.validated_data['mobile']
        code = self.generate_code()

        verifyCode = VerifyCode(code=code, mobile=mobile)
        verifyCode.save()
        return Response({"mobile": mobile,
                         "code": code})


class UserViewset(CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, GenericViewSet):
    serializer_class = UserRegSerializer

    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return UserDetailSerializer
        elif self.action == 'create':
            return UserRegSerializer

        return UserDetailSerializer

    def get_permissions(self):
        if self.action == 'retrieve':
            return [IsAuthenticated()]

        elif self.action == 'create':
            return []

        return []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict['token'] = jwt_encode_handler(payload)
        re_dict["name"] = user.name if user.name else user.username

        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.create(serializer.validated_data)

    def get_object(self):
        return self.request.user
