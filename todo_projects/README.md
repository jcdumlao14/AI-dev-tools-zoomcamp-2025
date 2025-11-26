# Homework 1: Introduction for AI Dev Tools Zoomcamp 2025
In this homework, we'll build an application with AI.
- use tool: ChatGPT
- build a TODO application in Django.
  
# Prerequisites
- Make sure Python is installed. Check by running:

```bash
python --version
```  
or
```bash
python3 --version
```
- Install VS Code and open your project folder.
  
# 🌟 Question 1: Install Django

**Open the terminal in VS Code (View → Terminal).**

**Create a virtual environment (optional but recommended):**
```bash
python -m venv venv
```
Activate it:
- Windows: `venv\Scripts\activate`
- Mac/Linux: `source venv/bin/activate`

Install Django:
```bash
pip install django
```
✅ **Answer for homework: `pip install django`**

# 🌟 Question 2: Create Project and App
**1. Create a Django project (replace `todo_project` with your project name):**
```bash
django-admin startproject todo_project
```
**2. Navigate into the project folder:**
```bash
cd todo_project
```
**3. Create an app (replace `tasks` with your app name):**
```bash
python manage.py startapp tasks
```
**4. Include the app in your project:**
- Open `todo_project/settings.py`
- Find `INSTALLED_APPS` and add your app:
```python
INSTALLED_APPS = [
    ...
    'tasks',
]
```
✅ **Answer for homework (file to edit): `settings.py`**

# 🌟 Question 3: Django Models

Models define the structure of your database.

**1. Open `tasks/models.py` and create a Todo model:**
```python
from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```
**2. Next steps:**
- Run migrations to create the database tables:
```bash
python manage.py makemigrations
python manage.py migrate
```
- Add the model to the admin panel (optional but good for testing):
```python
# tasks/admin.py
from django.contrib import admin
from .models import Todo

admin.site.register(Todo)

```
✅ **Answer for homework (next step): `Run migrations`**

# 🌟 Question 4: TODO Logic(views + URLs)
create the TODO logic inside views.py and hook it into urls.py.

## **Step 4.1 — Add logic inside tasks/views.py**

Create a simple CRUD (Create, Read, Update, Delete) system.

File: **tasks/views.py**

```python
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
```  
## **Step 4.2 — Register routes in tasks/urls.py**

File: **tasks/urls.py**
```bash
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add/", views.add_todo, name="add"),
    path("complete/<int:todo_id>/", views.toggle_complete, name="complete"),
    path("delete/<int:todo_id>/", views.delete_todo, name="delete"),
]

```  
## **Step 4.3 — Include them in main project URL**
File: **todo_project/urls.py**
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),
]

```
Where do you put the logic for the TODO app?

✅ **Answer for homework: `views.py`**

# 🌟 QUESTION 5 — Templates (base.html + home.html)

You must register your template directory inside `settings.py` under **TEMPLATES['DIRS']**.

## **Step 5.1 — Register templates directory**
File: **todo_project/settings.py**
```python
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],   # <--- ADD THIS
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

```
## **Step 5.2 — Create folder structure**
```csharp
todo_project/
    templates/
        base.html
        home.html
        add.html

```  
## **Step 5.3 — base.html**
File: **templates/base.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Todo App</title>
</head>
<body>
    <h1>📝 Simple Todo App</h1>
    <hr>

    {% block content %}
    {% endblock %}
</body>
</html>

```  
## **Step 5.4 — home.html**

File: **templates/home.html**
```html
{% extends "base.html" %}

{% block content %}
<h2>Your Tasks</h2>

<a href="{% url 'add' %}">➕ Add New Todo</a>

<ul>
    {% for todo in todos %}
        <li>
            <strong>{{ todo.title }}</strong> - {{ todo.description }}

            {% if todo.completed %}
                ✔ Completed
            {% else %}
                ❗ Pending
            {% endif %}

            <a href="{% url 'complete' todo.id %}">Toggle</a>
            <a href="{% url 'delete' todo.id %}">Delete</a>
        </li>
    {% empty %}
        <p>No tasks yet.</p>
    {% endfor %}
</ul>
{% endblock %}

``` 
## **Step 5.5 — add.html**

File: **templates/add.html**
```html
{% extends "base.html" %}

{% block content %}
<h2>Add Todo</h2>

<form method="POST">
    {% csrf_token %}
    <input type="text" name="title" placeholder="Task title" required><br><br>
    <textarea name="description" placeholder="Description (optional)"></textarea><br><br>

    <button type="submit">Add</button>
</form>

<br>
<a href="{% url 'home' %}">⬅ Back to Home</a>
{% endblock %}

```
✅ **Answer for homework: TEMPLATES['DIRS'] in project's settings.py**

# 🌟 QUESTION 6 — Tests

Django uses the `TestCase` class.

## Step 6.1 — Create tests in tasks/tests.py

File: **tasks/tests.py**

```python
from django.test import TestCase
from django.urls import reverse
from .models import Todo

class TodoTests(TestCase):

    def test_home_page_loads(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_add_todo(self):
        response = self.client.post(reverse("add"), {
            "title": "Test Todo",
            "description": "Testing add"
        })
        self.assertEqual(Todo.objects.count(), 1)

    def test_toggle_complete(self):
        todo = Todo.objects.create(title="Test", description="Test Desc")
        self.client.get(reverse("complete", args=[todo.id]))
        todo.refresh_from_db()
        self.assertTrue(todo.completed)

    def test_delete_todo(self):
        todo = Todo.objects.create(title="To delete")
        self.client.get(reverse("delete", args=[todo.id]))
        self.assertEqual(Todo.objects.count(), 0)

```  
## Step 6.2 — Run tests in terminal

Use this command:
```bash
python manage.py test
```
What is the command you use to run tests?

✅ **Answer for homework: python manage.py test**

# Running the Application

```nginx
python manage.py runserver
```  
# Open a browser and go to:

```arduino
http://127.0.0.1:8000/admin
```
# **GitHub**

**1. Initialize Git:**

```bash
git init
```
**2. Commit your code:**

```bash
git add .
git commit -m "Initial commit: Django TODO app"
```
3. **Push to GitHub in a folder `01-todo`.**
   
✅ Homework URL: https://github.com/jcdumlao14/AI-dev-tools-zoomcamp-2025/tree/main/todo_projects
