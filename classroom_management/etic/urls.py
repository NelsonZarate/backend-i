from django.urls import path
from . import views

urlpatterns = [
    path("signup", views.signup_view, name="signup"),
    path("signin", views.signin_view, name="signin"),
    path("logout", views.logout_view, name="logout"),
    path("add_grades", views.logout_view, name="add_grades"),
    path("", views.index_view, name="index"),
]
