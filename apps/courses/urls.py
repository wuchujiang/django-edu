from django.urls import re_path, path

from .views import CourseListView, CourseDetailView, CourseInfoView, CommentsView, AddComentsView

urlpatterns = [
    path("list/", CourseListView.as_view(), name="course_list"),

    # 课程详情页
    re_path(r'^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name="course_detail"),

    re_path(r'^info/(?P<course_id>\d+)/$', CourseInfoView.as_view(), name="course_info"),

    # 课程评论
    re_path(r'^comment/(?P<course_id>\d+)/$', CommentsView.as_view(), name="course_comments"),

    # 添加课程评论
    re_path(r'^add_comment/$', AddComentsView.as_view(), name="add_comment"),
]