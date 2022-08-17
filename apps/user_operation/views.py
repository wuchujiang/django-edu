from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from user_operation.models import UserFav
from user_operation.serializers import UserFavSerializers
from utils.permissions import IsOwnerOrReadOnly


class UserFavViewSet(ModelViewSet):
    serializer_class = UserFavSerializers
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

    def get_queryset(self):
        return UserFav.objects.filter(user=self.request.user)

