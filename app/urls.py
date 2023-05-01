from django.urls import path

from app.views import TaskListView

urlpatterns = [
    path('', TaskListView.as_view(), name='task-list'),
]

app_name = "app"
