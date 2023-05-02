from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from app.forms import TaskCreationForm
from app.models import Task, Tag


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    paginate_by = 5


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskCreationForm


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    fields = "__all__"


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("app:task-list")


@login_required
def task_toggle_done(done, pk):
    task = Task.objects.get(id=pk)
    task.done = not task.done
    task.save()

    return HttpResponseRedirect(
        reverse_lazy("app:task-list")
    )


class TagListView(LoginRequiredMixin, generic.ListView):
    model = Tag
    paginate_by = 5


class TagCreateView(LoginRequiredMixin, generic.CreateView):
    model = Tag
    fields = "__all__"


class TagUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Tag
    fields = "__all__"


class TagDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("app:tag-list")
