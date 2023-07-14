from django import forms

from todo_list.models import Tags, Task


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tags.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        label="Tags"
    )

    deadline = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={
            "placeholder": "Correct: 2023-07-28 20:00:00",
            "class": "form-control datetimepicker-input",
            "data-toggle": "datetimepicker",
            "data-target": "#date3",
        }),
        help_text="Optional deadline datetime if a task should be done until some datetime",
        required=False
    )

    class Meta:
        model = Task
        fields = ["content", "deadline", "done_or_not", "tags"]


class TagsForm(forms.ModelForm):

    class Meta:
        model = Tags
        fields = ["name"]
