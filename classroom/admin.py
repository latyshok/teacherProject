from django.contrib import admin

from classroom.models import Subject, Student, Teacher


class BasePersonAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'phone',
        'first_name',
        'last_name',
        'middle_name',
    )

    raw_id_fields = (
        'user',
        'subjects',
    )


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )


@admin.register(Teacher)
class TeacherAdmin(BasePersonAdmin):
    pass


@admin.register(Student)
class StudentAdmin(BasePersonAdmin):
    pass
