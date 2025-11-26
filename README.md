# AI-dev-tools-zoomcamp-2025
AI Dev Tools Zoomcamp 2025

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
# Question 1: Install Django
1. Open the terminal in VS Code (View → Terminal).
2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
```
Activate it:
- Windows: `venv\Scripts\activate`
- Mac/Linux: `source venv/bin/activate`
3. Install Django using AI-suggested command:
```bash
pip install django
```
✅ Answer for homework: `pip install django`
# Question 2: Create Project and App
1. Create a Django project (replace `todo_project` with your project name):
```bash
django-admin startproject todo_project
```
2. Navigate into the project folder:
```bash
cd todo_project
```
3. Create an app (replace `tasks` with your app name):
```bash
python manage.py startapp tasks
```
4. Include the app in your project:
- Open `todo_project/settings.py`
- Find `INSTALLED_APPS` and add your app:
```python
INSTALLED_APPS = [
    ...
    'tasks',
]
```
✅ Answer for homework (file to edit): settings.py
# Question 3: Django Models
Models define the structure of your database.
1. Open `tasks/models.py` and create a Todo model:
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
2. Next steps:
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
✅ Answer for homework (next step): `Run migrations`

# Question 4: Templates

You’ll deal with this later, so skip for now.

# Step 4: Run the Application
1. Create a superuser to access the admin panel:
```bash
python manage.py createsuperuser
```  
2. Run the server:
```bash
python manage.py runserver
```  
3. Open a browser and go to:
```arduino
http://127.0.0.1:8000/admin
```  
- Log in with the superuser credentials.
- You should see your Todo model.
# Step 5: GitHub
1. Initialize Git:
```bash
git init
```
2. Commit your code:
```bash
git add .
git commit -m "Initial commit: Django TODO app"
```
3. Push to GitHub in a folder `01-todo`.
   
✅ Homework URL: Provide the GitHub folder link.
