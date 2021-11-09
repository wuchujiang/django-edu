from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from pure_pagination import Paginator, PageNotAnInteger

from .operation.models import UserCourse
from .utils.mixin_utils import LoginRequiredMixin
from .operation.models import UserFavorite
from .models import Course


class CourseListView(View):
    def get(self, request):
        all_courses = Course.objects.all().order_by("-add_time")

        hot_course = Course.objects.all().order_by("-click_nums")[:3]

        # 课程搜索
        search_words = request.GET.get("keywords", "")
        if search_words:
            all_courses = all_courses.filter(
                Q(name__icontains=search_words) | Q(desc__icontains=search_words) | Q(detail__icontains=search_words))

        # 课程排序
        sort = request.GET.get("sort", "")
        if sort:
            if sort == "students":
                all_courses = all_courses.order_by("-students")
            elif sort == "hot":
                all_courses = all_courses.order_by("-click_nums")

        # 课程分页

        try:
            page = request.GET.get("page", 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_courses, 12, request=request)

        courses = p.page(page)
        return render(request, "course-list.html", {
            "all_courses": courses,
            "sort": sort,
            "hot_courses": hot_course
        })


class CourseDetailView(View):
    """
    课程详情页
    """
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))

        # 增加课程点击数
        course.click_nums +=1
        course.save()

        # 是否收藏课程
        has_fav_course = False
        has_fav_org = False

        if request.use.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course.id, fav_type=1):
                has_fav_course = True

            if UserFavorite.objects.filter(user=request.user, fav_id=course.course_org.id,fav_type=2):
                has_fav_org = True

        tag = course.tag

        if tag:
            relate_course = Course.objects.filter(tag=tag)[:1]
        else:
            relate_course = []

        return render(request, "course-detail.html", {
            "course": course,
            "relate_coures": relate_course,
            "has_fav_course": has_fav_course,
            "has_fav_org": has_fav_org
        })


class CourseInfoView(LoginRequiredMixin,View):
    """
    课程章节信息
    """
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        course.students +=1
        course.save()

        # 查询用户是否已经关联了该课程
        user_courses = UserCourse.objects
