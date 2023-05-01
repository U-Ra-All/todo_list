from django import forms

from app.models import Task


class TaskCreationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["content", "deadline_datetime", "done", "tags"]
        widgets = {
            "deadline_datetime": forms.DateTimeInput(
                attrs={"placeholder": "e.g. 2006-10-25 14:30"}
            )
        }

        labels = {
            "deadline_datetime": "Deadline date and time (optional)"
        }
