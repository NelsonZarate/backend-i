from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Classroom(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(User, related_name="classrooms")  # Alunos em uma turma

class Course(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name="courses")  # Professor da disciplina
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name="courses")

class Grade(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="grades")  # Aluno que recebeu a nota
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="grades")  # Disciplina associada
    score = models.FloatField()
    feedback = models.TextField(blank=True, null=True)  # Comentários opcionais do professor
