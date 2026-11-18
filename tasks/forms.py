from django import forms
from .models import Tag, Task


class DateTimeLocalInput(forms.DateTimeInput):
    input_type = "datetime-local"


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["content", "deadline", "tags"]
        labels = {
            "content": "Task description",
            "deadline": "Deadline (optional)",
            "tags": "Tags (optional)",
        }
        widgets = {
            "content": forms.Textarea(attrs={"rows": 4, "placeholder": "What needs to get done?"}),
            "deadline": DateTimeLocalInput(format="%Y-%m-%dT%H:%M"),
            "tags": forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["tags"].queryset = Tag.objects.all()
        self.fields["deadline"].input_formats = ["%Y-%m-%dT%H:%M"]


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
        widgets = {"name": forms.TextInput(attrs={"placeholder": "e.g. work"})}
