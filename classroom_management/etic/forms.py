from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import User,Course, Classroom 

class EticUserCreationForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ('username', 'role') 


class ClassroomForm(forms.ModelForm):
    class Meta:
        model = Classroom
        fields = ['name', 'students']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'teacher', 'classroom']