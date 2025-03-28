from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Grade, Course,User,Classroom
from .forms import EticUserCreationForm
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


def signup_view(request):
    if request.method == "POST":
        form = EticUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("signin")
    else:
        form = EticUserCreationForm()
    return render(request, "registration/signup.html", {"form": form})

def signin_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
            # Redirect based on role
            if user.is_superuser or user.role == 'admin':
                return redirect('admin_dashboard')
            elif user.role == 'teacher':
                return redirect('teacher_dashboard')
            else:  # student
                return redirect('student_view')
    else:
        form = AuthenticationForm(request)
    
    return render(request, "registration/signin.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("signin")

def index_view(request):
    return render(request, "etic/index.html")


def is_teacher(user):
    return user.is_authenticated and user.role == "teacher"

@login_required
@user_passes_test(is_teacher)
def add_grade(request, course_id, student_id):
    course = get_object_or_404(Course, id=course_id)
    student = get_object_or_404(User, id=student_id, role="student")
    
    if request.method == "POST":
        score = request.POST.get("score")
        feedback = request.POST.get("feedback", "")
        Grade.objects.create(student=student, course=course, score=score, feedback=feedback)
        return redirect("course_detail", course_id=course.id)

    return render(request, "etic/add_grades.html", {"course": course, "student": student})


def student_view(request):
    if request.method == "GET":
        return render(request, "etic/grades_student.html")

def admin_dashboard_view(request):
    if request.method == "GET":
        return render(request, "etic/admin_dashboard.html")

def teacher_dashboard(request):
    if request.method == "GET":
        return render(request, "etic/teacher_dashboard.html")



class TeacherDashboardView(LoginRequiredMixin, ListView):
    template_name = 'etic/teacher/teacher_dashboard.html'
    context_object_name = 'classrooms'

    def get_queryset(self):
        # Get only classrooms where current user is the teacher
        return Classroom.objects.filter(
            courses__teacher=self.request.user
        ).distinct()

class StudentListView(LoginRequiredMixin, ListView):
    template_name = 'etic/teacher/student_list.html'
    
    def get_queryset(self):
        classroom = self.kwargs['classroom_id']
        return User.objects.filter(
            classrooms=classroom,
            role='student'
        )

class AddGradeView(LoginRequiredMixin, CreateView):
    model = Grade
    fields = ['score', 'feedback']
    template_name = 'etic/teacher/add_grade.html'
    
    def form_valid(self, form):
        form.instance.teacher = self.request.user
        form.instance.student = User.objects.get(pk=self.kwargs['student_id'])
        form.instance.course = Course.objects.get(pk=self.kwargs['course_id'])
        return super().form_valid(form)