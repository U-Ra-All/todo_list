from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from app.forms import TaskCreationForm
from app.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 5


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskCreationForm


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("app:task-list")


class TaskToggleDone(generic.UpdateView):
    model = Task
    fields = "__all__"

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        task = get_object_or_404(Task, id=pk)
        task.done = not task.done
        task.save()

        return redirect("app:task-list")


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 5


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("app:tag-list")
