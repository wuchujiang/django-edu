from django.urls import re_path, path

from .views import CourseListView

urlpatterns = [
    path("/list/", CourseListView.as_view(), name="course_list")
]