from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add/", views.add_todo, name="add"),
    path("complete/<int:todo_id>/", views.toggle_complete, name="complete"),
    path("delete/<int:todo_id>/", views.delete_todo, name="delete"),
]
