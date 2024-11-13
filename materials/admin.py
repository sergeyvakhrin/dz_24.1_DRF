from django.contrib import admin

from materials.models import Lesson, Course


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'lesson_name', 'description', 'preview', 'video', 'course', 'owner']
    list_display_links = ['id', 'lesson_name', 'description']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'course_name', 'preview', 'description', 'owner']
    list_display_links = ['id', 'course_name', 'preview', 'description', 'owner']
