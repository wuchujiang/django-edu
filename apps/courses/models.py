from django.db import models
from django.db.models import CASCADE
from django.utils import timezone

from DUEditor.models import UEditorField

# Create your models here.

# 课程
from organization.models import Teacher, CourseOrg


class Course(models.Model):
    course_org = models.ForeignKey(CourseOrg, verbose_name=u"课程机构", null=True, blank=True, on_delete=CASCADE)
    name = models.CharField(max_length=50, verbose_name=u"课程名")
    desc = models.CharField(max_length=300, verbose_name=u"课程描述")
    detail = UEditorField(verbose_name=u"课程详情", width=600, height=300, imagePath="courses/ueditor/",
                          filePath="courses/ueditor/", default="")
    is_banner = models.BooleanField(default=False, verbose_name=u"是否轮播")
    teacher = models.ForeignKey(Teacher, verbose_name=u"讲师", null=True, blank=True, on_delete=CASCADE)
    degree = models.CharField(verbose_name=u"难度", choices=(("cj", "初级"), ("zj", "中级"), ("gj", "高级")), max_length=2)
    learn_times = models.IntegerField(default=0, verbose_name=u"学习时长(分钟数)")
    students = models.IntegerField(default=0, verbose_name=u"学习人数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏人数")
    image = models.ImageField(upload_to="courses/%Y/%m", verbose_name=u"封面图", max_length=100)
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    category = models.CharField(default=u"后端开发", verbose_name=u"课程类别", max_length=20)
    tag = models.CharField(default="", verbose_name=u"课程标签", max_length=10)
    youneed_know = models.CharField(default="", verbose_name=u"课程须知", max_length=300)
    teacher_tell = models.CharField(default="", verbose_name=u"老师告诉你", max_length=300)

    add_time = models.DateTimeField(default=timezone.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程"
        verbose_name_plural = verbose_name

    # 获取课程章节数
    def get_zj_nums(self):
        return self.lesson_set.all().count()

    get_zj_nums.short_description = "章节数"

    def go_to(self):
        from django.utils.safestring import mark_safe
        return mark_safe("<a href='http://www.projectsedu.com'>跳转</>")

    go_to.short_description = "跳转"

    def get_learn_users(self):
        return self.usercourse_set.all()[:5]

    def get_course_lesson(self):
        # 获取课程所有章节
        return self.lesson_set.all()

    def __unicode__(self):
        return self.name


# 轮播banner
class Banner(Course):
    class Meta:
        verbose_name = u"轮播课程"
        verbose_name_plural = verbose_name
        proxy = True


# 章节
class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"课程", on_delete=CASCADE)
    name = models.CharField(max_length=100, verbose_name=u"章节名")
    learn_times = models.IntegerField(default=0, verbose_name=u"学习时长（分钟数）")
    add_time = models.DateTimeField(default=timezone.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"章节"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

    def get_lesson_video(self):
        return self.video_set.all()


# 章节视频
class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name=u"章节", on_delete=CASCADE)
    name = models.CharField(max_length=100, verbose_name=u"视频名")
    learn_times = models.IntegerField(default=0, verbose_name=u"学习时长（分钟数）")
    url = models.CharField(max_length=200, default="", verbose_name=u"访问地址")
    add_time = models.DateTimeField(default=timezone.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"视频"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


# 课程资源
class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"课程", on_delete=CASCADE)
    name = models.CharField(max_length=100, verbose_name=u"名称")
    download = models.FileField(upload_to="course/resource/%Y/%m", verbose_name=u"资源文件", max_length=100)
    add_time = models.DateTimeField(default=timezone.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程资源"
        verbose_name_plural = verbose_name
