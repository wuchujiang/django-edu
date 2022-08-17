"""edu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve

from edu.settings import MEDIA_ROOT

from rest_framework_jwt.views import obtain_jwt_token

from goods.views import GoodsListViewSet, GoodsListView
from user_operation.views import UserFavViewSet
from users.views import SmsCodeViewset, UserViewset


urlpatterns = [
    url(r'^login', obtain_jwt_token),
    url(r'^goods$', GoodsListViewSet.as_view({"get":"list"})),
    url(r'^good2$', GoodsListView.as_view()),
    url(r'^codes$', SmsCodeViewset.as_view({'post': 'create'})),
    url(r'^users$', UserViewset.as_view({'post': 'create'})),
    url(r'^users/(?P<pk>\d+)$', UserViewset.as_view({'get': 'retrieve'})),
    url(r'^goods/(?P<pk>\d+)$', GoodsListViewSet.as_view({"get": "retrieve"})),
    url(r'^users/fav$', UserFavViewSet.as_view({"get": "list", "post":"create" })),
    url(r'^users/fav/(?P<pk>\d+)$', UserFavViewSet.as_view({"get": "retrieve", "delete": "destroy"}))

]

