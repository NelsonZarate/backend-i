from django.urls import path
from django.contrib.auth.views import LoginView
from . import views
from .views import TeacherDashboardView, StudentListView, AddGradeView

urlpatterns = [
    path("signup", views.signup_view, name="signup"),
    path("signin", views.signin_view, name="signin"),
    path("add_grades", views.add_grade, name="add_grades"),
    path("student_view", views.student_view, name="student_view"),
    path("admin_dashboard", views.admin_dashboard_view, name="admin_dashboard"),
    path("teacher_dashboard", views.teacher_dashboard, name="teacher_dashboard"),
    path("logout", views.logout_view, name="logout"),
    path("", views.index_view, name="index"),
]

#teacher dashboard utl patterns
urlpatterns = [
    path('teacher/', TeacherDashboardView.as_view(), name='teacher_dashboard'),
    path('teacher/classroom/<int:classroom_id>/', StudentListView.as_view(), name='student_list'),
    path('teacher/grade/<int:course_id>/<int:student_id>/', AddGradeView.as_view(), name='add_grade'),
]