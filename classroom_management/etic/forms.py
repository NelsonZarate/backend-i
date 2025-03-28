from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import User  # Your custom user model

class EticUserCreationForm(UserCreationForm):
    class Meta:
        model = User  # Your custom user model
        fields = ('username', 'role')  # Include any additional fields you want in the form