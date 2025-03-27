from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import PermissionDenied
from django.contrib.auth import get_user_model

class User(AbstractUser):
    ROLE_CHOICES = [
        ("admin", "Administrator"),
        ("teacher", "Teacher"), 
        ("student", "Student"),
    ]
    role = models.CharField(
        max_length=10, 
        choices=ROLE_CHOICES, 
        default="student"
    )
    
    def is_admin(self):
        return self.role == "admin" or self.is_superuser
    
    def is_teacher(self):
        return self.role == "teacher"
    
    def is_student(self):
        return self.role == "student"

class Classroom(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(
        get_user_model(), 
        related_name="classrooms",
        limit_choices_to={"role": "student"}
    )

class Course(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="courses",
        limit_choices_to={"role": "teacher"}
    )
    classroom = models.ForeignKey(
        Classroom,
        on_delete=models.CASCADE,
        related_name="courses"
    )

class Grade(models.Model):
    student = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="grades",
        limit_choices_to={"role": "student"}
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="grades"
    )
    score = models.FloatField()
    feedback = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.course.teacher == self.student:
            super().save(*args, **kwargs)
        else:
            raise PermissionDenied("Teachers cannot grade themselves")