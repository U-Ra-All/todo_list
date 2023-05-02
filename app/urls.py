from django.urls import path

from app.views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    task_toggle_done,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView
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
    path(
        "/tags/",
        TagListView.as_view(),
        name="tags-list"
    ),
    path(
        "/create/",
        TagCreateView.as_view(),
        name="tags-create"
    ),
    path(
        "/<int:pk>/update/",
        TagUpdateView.as_view(),
        name="tags-update",
    ),
    path(
        "/<int:pk>/delete/",
        TagDeleteView.as_view(),
        name="tags-delete",
    ),
]

app_name = "app"
