from django.contrib import admin
from .models import CourseType, Group, Student


@admin.register(CourseType)
class CourseTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'surname',
        'email'
    )

    search_fields = ('name', 'surname', 'email',)

