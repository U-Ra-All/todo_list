from django.urls import path

from app.views import TaskListView, TaskCreateView, task_toggle_done

urlpatterns = [
    path(
        "",
        TaskListView.as_view(),
        name="task-list"
    ),
    path(
        "/create",
        TaskCreateView.as_view(),
        name="task-create"
    ),
    path(
        "/<int:pk>/toggle-done/",
        task_toggle_done,
        name="task-toggle-done",
    ),
]

app_name = "app"
