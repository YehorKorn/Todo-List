from django.db import models


class Tags(models.Model):
    name = models.CharField(max_length=64, help_text="Symbolizes the theme of the task")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "tag"
        verbose_name_plural = "tags"


class Task(models.Model):
    content = models.CharField(max_length=256, help_text="describes what you should do.")
    datetime = models.DateTimeField(help_text="when a task was created", auto_now_add=True)
    deadline = models.DateTimeField(
        help_text="optional deadline datetime if a task should be done until some datetime",
        null=True,
        blank=True,
    )
    done_or_not = models.BooleanField(help_text="Marks if the task is done or not", default=False)
    tags = models.ManyToManyField(Tags, related_name="tasks")

    def __str__(self):
        return (f"{self.content} (Created: {self.datetime}; {self.deadline})\n"
                f"Task is done - {self.done_or_not}.    Tags: {self.tags.name}")

    class Meta:
        ordering = ["done_or_not", "-datetime"]
        verbose_name = "task"
        verbose_name_plural = "tasks"
