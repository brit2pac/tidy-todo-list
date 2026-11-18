from django.urls import path
from . import views

urlpatterns = [
    path("", views.task_list, name="home"),
    path("tasks/add/", views.task_create, name="task-add"),
    path("tasks/<int:pk>/edit/", views.task_update, name="task-edit"),
    path("tasks/<int:pk>/delete/", views.task_delete, name="task-delete"),
    path("tasks/<int:pk>/toggle/", views.task_toggle, name="task-toggle"),
    path("tags/", views.tag_list, name="tag-list"),
    path("tags/add/", views.tag_create, name="tag-add"),
    path("tags/<int:pk>/edit/", views.tag_update, name="tag-edit"),
    path("tags/<int:pk>/delete/", views.tag_delete, name="tag-delete"),
]
