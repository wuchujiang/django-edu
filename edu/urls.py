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
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve

from edu.settings import MEDIA_ROOT
from users.views import IndexView, LoginView, LogoutView, RegisterView, ActiveUserView, ForgetPwdView, ResetView, \
    ModifyPwdView

urlpatterns = [
    path('', IndexView.as_view(),name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('captcha/', include('captcha.urls')),
    re_path(r'^active/(?P<active_code>.*)$', ActiveUserView.as_view(), name='user_active'),
    path('forget/', ForgetPwdView.as_view(), name='forget_pwd'),
    re_path(r'^reset/(?P<active_code>.*)$', ResetView.as_view(), name='reset_pwd'),
    path(r'modify_pwd/', ModifyPwdView.as_view(), name='modify_pwd'),

    path('ueditor/', include('DUEditor.urls')),
    path('admin/', admin.site.urls),

    path("course/", include(("courses.urls", "courses"), namespace='course')),
    path('org/', include(('organization.urls', 'organization'), namespace='org')),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    re_path(r'^media/(?P<path>.*)$', serve, {"document_root":MEDIA_ROOT}),

]
