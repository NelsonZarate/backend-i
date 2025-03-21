from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView,TemplateView

from todo.models import Task

# Create your views here.
def index(request):
    tasks = Task.objects.all()
    return render(request,"todo/index.html", {"foo":"World", "tasks":tasks})

class TaskListView(ListView):
    model = Task

class IndexView(TemplateView):
    http_method_names = ['get']
    template_name = "todo/index.html"