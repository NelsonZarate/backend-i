from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse,reverse_lazy
from .models import Grade, Course,User,Classroom
from .forms import EticUserCreationForm, ClassroomForm, CourseForm
from django.views.generic import ListView, CreateView, TemplateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import View
from django.db.models import Prefetch 
from collections import defaultdict  
import logging
logger = logging.getLogger('etic')

def signup_view(request):
    if request.method == "POST":
        form = EticUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            logger.info(f"New user '{user.username}' registered with role '{user.role}'.")
            return redirect("admin_dashboard")
        else:
            logger.warning("User registration failed due to invalid form input.")
    
    else:
        form = EticUserCreationForm()

    return render(request, "admin/admin_dashboard.html", {"form": form})

def signin_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            logger.info(f"User '{user.username}' logged in successfully.")

            if user.is_superuser or user.role == 'admin':
                return redirect('admin_dashboard')
            elif user.role == 'teacher':
                return redirect('teacher_dashboard')
            else:
                return redirect('student_dashboard')
        else:
            logger.warning(f"Failed login attempt for username: {request.POST.get('username')}")

    else:
        form = AuthenticationForm(request)

    return render(request, "registration/signin.html", {"form": form})

def signin_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.is_superuser or user.role == 'admin':
                return redirect('admin_dashboard')
            elif user.role == 'teacher':
                return redirect('teacher_dashboard')
            else:
                return redirect('student_dashboard')
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
        try:
            score = request.POST.get("score")
            feedback = request.POST.get("feedback", "")
            Grade.objects.create(student=student, course=course, score=score, feedback=feedback)
            logger.info(f"Teacher '{request.user.username}' added grade {score} for student '{student.username}' in course '{course.name}'")
            return redirect("course_detail", course_id=course.id)
        except Exception as e:
            logger.error(f"Error adding grade: {str(e)}", exc_info=True)

    return render(request, "teacher/add_grade.html", {"course": course, "student": student})


class StudentListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = User
    template_name = 'teacher/student_list.html'
    
    def test_func(self):
        return self.request.user.is_teacher()
    
    def get_queryset(self):
        classroom = get_object_or_404(Classroom, pk=self.kwargs['pk'])
        return classroom.students.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        student = self.request.user
        context['classroom'] = get_object_or_404(Classroom, pk=self.kwargs['pk'])
        logger.info(f"Student '{student.username}' accessed their dashboard.")

        return context

class AdminDashboardView(UserPassesTestMixin, View):
    template_name = "admin/admin_dashboard.html"
    
    def test_func(self):
        return self.request.user.is_superuser or self.request.user.role == 'admin'
    
    def get_context_data(self):
        context = {
            'all_users': User.objects.all(),
            'teachers': User.objects.filter(role='teacher'),
            'students': User.objects.filter(role='student'),
            'admins': User.objects.filter(role='admin'),
            'classrooms': Classroom.objects.all(),
            'courses': Course.objects.all(),
            'form': EticUserCreationForm(),
            'classroom_form': ClassroomForm(),
            'course_form': CourseForm(),
        }
        return context
    
    def get(self, request, *args, **kwargs):

        logger.info(f"Admin '{request.user.username}' accessed the admin dashboard.")
        return render(request, self.template_name, self.get_context_data())
    
    def post(self, request, *args, **kwargs):
        if 'create_user' in request.POST:
            form = EticUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('admin_dashboard')

        elif 'create_classroom' in request.POST:
            classroom_form = ClassroomForm(request.POST)
            if classroom_form.is_valid():
                classroom_form.save()
                return redirect('admin_dashboard')
        

        elif 'create_course' in request.POST:
            course_form = CourseForm(request.POST)
            if course_form.is_valid():
                course_form.save()
                return redirect('admin_dashboard')
        

        context = self.get_context_data()
        if 'create_user' in request.POST:
            context['form'] = form
        elif 'create_classroom' in request.POST:
            context['classroom_form'] = classroom_form
        elif 'create_course' in request.POST:
            context['course_form'] = course_form
            
        return render(request, self.template_name, context)
    

class TeacherDashboardView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Classroom
    template_name = 'teacher/teacher_dashboard.html'
    context_object_name = 'classrooms'

    def test_func(self):
        return self.request.user.is_teacher()

    def get_queryset(self):
        return Classroom.objects.filter(
            courses__teacher=self.request.user
        ).distinct()
    
class ClassroomStudentsView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'teacher/classroom_students.html'

    def test_func(self):
        return self.request.user.is_teacher()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        classroom = get_object_or_404(Classroom, pk=self.kwargs['classroom_id'])
        students = classroom.students.all()
        courses = Course.objects.filter(
            classroom=classroom,
            teacher=self.request.user
        )
        
        # Get all grades grouped by student and course
        grades = Grade.objects.filter(
            student__in=students,
            course__in=courses
        ).order_by('student', 'course', '-id').distinct('student', 'course')
        
        # Organize grades by student
        grades_by_student = {}
        for grade in grades:
            if grade.student_id not in grades_by_student:
                grades_by_student[grade.student_id] = {}
            grades_by_student[grade.student_id][grade.course_id] = grade
        
        context.update({
            'classroom': classroom,
            'students': students,
            'courses': courses,
            'grades_by_student': grades_by_student
        })
        return context

class AddGradeView(LoginRequiredMixin, UserPassesTestMixin, View):
    template_name = 'teacher/add_grade.html'
    
    def test_func(self):
        return self.request.user.is_teacher()

    def get(self, request, *args, **kwargs):
        # Get or create grade instance
        grade, created = Grade.objects.get_or_create(
            student_id=self.kwargs['student_id'],
            course_id=self.kwargs['course_id'],
            defaults={'score': 0, 'feedback': ''}
        )
        
        context = {
            'student': get_object_or_404(User, pk=self.kwargs['student_id']),
            'course': get_object_or_404(Course, pk=self.kwargs['course_id']),
            'grade': grade,
            'is_editing': not created
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        grade, created = Grade.objects.get_or_create(
            student_id=self.kwargs['student_id'],
            course_id=self.kwargs['course_id']
        )
        
        grade.score = request.POST.get('score')
        grade.feedback = request.POST.get('feedback', '')
        grade.save()
        
        return redirect('classroom_students', classroom_id=grade.course.classroom.id)

class EditClassroomView(UserPassesTestMixin, UpdateView):
    model = Classroom
    form_class = ClassroomForm
    template_name = 'admin/edit_classroom.html'
    success_url = reverse_lazy('admin_dashboard')
    
    def test_func(self):
        return self.request.user.is_superuser or self.request.user.role == 'admin'

class DeleteClassroomView(UserPassesTestMixin, DeleteView):
    model = Classroom
    template_name = 'admin/confirm_delete.html'
    success_url = reverse_lazy('admin_dashboard')
    
    def test_func(self):
        return self.request.user.is_superuser or self.request.user.role == 'admin'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_type'] = 'classroom'
        return context

class EditCourseView(UserPassesTestMixin, UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'admin/edit_course.html'
    success_url = reverse_lazy('admin_dashboard')
    
    def test_func(self):
        return self.request.user.is_superuser or self.request.user.role == 'admin'

class DeleteCourseView(UserPassesTestMixin, DeleteView):
    model = Course
    template_name = 'admin/confirm_delete.html'
    success_url = reverse_lazy('admin_dashboard')

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.role == 'admin'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_type'] = 'course'
        return context

    def delete(self, request, *args, **kwargs):
        course = self.get_object()
        user = request.user

        try:
            logger.info(f"User {user} (ID: {user.id}) is deleting course: {course.name} (ID: {course.id})")
            response = super().delete(request, *args, **kwargs)
            logger.info(f"Course {course.name} (ID: {course.id}) successfully deleted by {user}.")
            return response
        except Exception as e:
            logger.error(f"Error deleting course {course.name} (ID: {course.id}): {e}", exc_info=True)
            return redirect(self.success_url)

class StudentDashboardView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'student/dashboard.html'

    def test_func(self):
        return self.request.user.is_student()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        student = self.request.user
        
        # Get all classrooms the student is in with related courses
        classrooms = Classroom.objects.filter(students=student).prefetch_related(
            Prefetch('courses', queryset=Course.objects.select_related('teacher'))
        ).distinct()
        
        # Get all grades for this student with related course info
        grades = Grade.objects.filter(student=student).select_related(
            'course', 'course__classroom', 'course__teacher'
        ).order_by('-id')
        
        # Organize grades by course
        grades_by_course = defaultdict(list)
        for grade in grades:
            grades_by_course[grade.course_id].append(grade)
        
        # Get classmates (students in the same classrooms) with their classrooms
        classmates = User.objects.filter(
            classrooms__in=classrooms  # Changed from classroom__in to classrooms__in
        ).exclude(id=student.id).distinct().prefetch_related('classrooms')
        
        # Calculate average grade per course
        course_stats = {}
        for course_id, grade_list in grades_by_course.items():
            scores = [g.score for g in grade_list]
            course_stats[course_id] = {
                'average': sum(scores) / len(scores) if scores else 0,
                'count': len(scores),
                'latest': grade_list[0]  # Most recent grade
            }
        
        context.update({
            'student': student,
            'classrooms': classrooms,
            'grades': grades,
            'grades_by_course': dict(grades_by_course),
            'course_stats': course_stats,
            'classmates': classmates,
        })
        return context
