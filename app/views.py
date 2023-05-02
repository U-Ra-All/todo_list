from django.http import HttpResponseRedirect
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


def task_toggle_done(done, pk):
    task = Task.objects.get(id=pk)
    task.done = not task.done
    task.save()

    return HttpResponseRedirect(
        reverse_lazy("app:task-list")
    )


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
