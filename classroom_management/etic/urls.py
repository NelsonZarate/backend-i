from django.urls import path
from django.contrib.auth.views import LoginView
from .views import (
    signup_view,
    signin_view,
    logout_view,
    index_view,
    AdminDashboardView,
    TeacherDashboardView,
    ClassroomStudentsView,
    AddGradeView,
    EditCourseView,
    DeleteCourseView,
    EditClassroomView,
    DeleteClassroomView,
    StudentListView,
    StudentDashboardView
)

urlpatterns = [
    # Auth routes
    path("signin/", signin_view, name="signin"),
    path("logout/", logout_view, name="logout"),
    
    # Role-based dashboards
    path("admin-dashboard/", AdminDashboardView.as_view(), name="admin_dashboard"),
    path("admin-create-new-user/", signup_view, name="signup"),
    
    # Teacher routes 
    path("teacher/", TeacherDashboardView.as_view(), name="teacher_dashboard"),
    path("teacher/classroom/<int:classroom_id>/", ClassroomStudentsView.as_view(), name="classroom_students"),
    path("teacher/course/grade/<int:course_id>/<int:student_id>/grade/", AddGradeView.as_view(), name="add_grade"),
    path('teacher/classroom/<int:pk>/students/', StudentListView.as_view(), name='student_list'),

    #student list view
    path('student/dashboard/', StudentDashboardView.as_view(), name='student_dashboard'),
   
    # Classroom management routes
    path('admin-dashboard/course/edit/<int:pk>/', EditCourseView.as_view(), name='edit_course'),
    path('admin-dashboard/course/delete/<int:pk>/', DeleteCourseView.as_view(), name='delete_course'),
    path('admin-dashboard/classroom/edit/<int:pk>/', EditClassroomView.as_view(), name='edit_classroom'),
    path('admin-dashboard/classroom/delete/<int:pk>/', DeleteClassroomView.as_view(), name='delete_classroom'),
    
    # Main pages
    path("", index_view, name="index"),
    
]