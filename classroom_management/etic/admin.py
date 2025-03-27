from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Classroom, Course, Grade

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'role', 'is_staff')
    list_filter = ('role', 'is_staff', 'is_active')
    fieldsets = UserAdmin.fieldsets + (
        ("Role", {"fields": ("role",)}),
    )
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        elif request.user.is_admin():
            return qs.filter(role__in=["teacher", "student"])
        elif request.user.is_teacher():
            return qs.filter(role="student")
        return qs.none()

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher', 'classroom')
    list_filter = ('teacher', 'classroom')
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser or request.user.is_admin():
            return qs
        return qs.filter(teacher=request.user)

class GradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'score')
    list_filter = ('course',)
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser or request.user.is_admin():
            return qs
        return qs.filter(course__teacher=request.user)

admin.site.register(User, CustomUserAdmin)
admin.site.register(Classroom)
admin.site.register(Course, CourseAdmin)
admin.site.register(Grade, GradeAdmin)