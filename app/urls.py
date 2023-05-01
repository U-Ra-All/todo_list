from django.urls import path

from app.views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    task_toggle_done,
)

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
        "/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update",
    ),
    path(
        "/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete",
    ),
    path(
        "/<int:pk>/toggle-done/",
        task_toggle_done,
        name="task-toggle-done",
    ),
]

app_name = "app"
