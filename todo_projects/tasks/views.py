from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo

def home(request):
    todos = Todo.objects.all()
    return render(request, "home.html", {"todos": todos})

def add_todo(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        Todo.objects.create(title=title, description=description)
        return redirect("home")
    return render(request, "add.html")

def toggle_complete(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.completed = not todo.completed
    todo.save()
    return redirect("home")

def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.delete()
    return redirect("home")

