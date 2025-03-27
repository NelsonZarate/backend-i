from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Grade, Course,User

def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("signin")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})

def signin_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("index")
    else:
        form = AuthenticationForm()
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

    return render(request, "etic/add_grade.html", {"course": course, "student": student})

