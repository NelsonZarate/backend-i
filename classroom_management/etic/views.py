from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

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