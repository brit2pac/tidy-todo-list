from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from .forms import TagForm, TaskForm
from .models import Tag, Task


def task_list(request):
    tasks = Task.objects.prefetch_related("tags")
    return render(request, "tasks/task_list.html", {
        "tasks": tasks,
        "open_tasks": tasks.filter(is_done=False),
        "done_tasks": tasks.filter(is_done=True),
    })


def task_create(request):
    form = TaskForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("home")
    return render(request, "tasks/task_form.html", {"form": form, "title": "Add task"})


def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    form = TaskForm(request.POST or None, instance=task)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("home")
    return render(request, "tasks/task_form.html", {"form": form, "title": "Update task"})


@require_POST
def task_delete(request, pk):
    get_object_or_404(Task, pk=pk).delete()
    return redirect("home")


@require_POST
def task_toggle(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done
    task.save(update_fields=["is_done"])
    return redirect("home")


def tag_list(request):
    return render(request, "tasks/tag_list.html", {"tags": Tag.objects.all()})


def tag_create(request):
    form = TagForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("tag-list")
    return render(request, "tasks/tag_form.html", {"form": form, "title": "Add tag"})


def tag_update(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    form = TagForm(request.POST or None, instance=tag)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("tag-list")
    return render(request, "tasks/tag_form.html", {"form": form, "title": "Update tag"})


@require_POST
def tag_delete(request, pk):
    get_object_or_404(Tag, pk=pk).delete()
    return redirect("tag-list")
