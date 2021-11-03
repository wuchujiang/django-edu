from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from pure_pagination import Paginator, PageNotAnInteger

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
