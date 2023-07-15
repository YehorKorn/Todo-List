from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todo_list.forms import TaskForm, TagsForm
from todo_list.models import Task, Tags


class TaskList(generic.ListView):
    model = Task
    queryset = Task.objects.all().prefetch_related("tags")
    context_object_name = "task_list"
    template_name = "todo_list/index.html"


class TaskCreateView(generic.CreateView):
    model = Task
    queryset = Task.objects.prefetch_related("tags")
    form_class = TaskForm
    success_url = reverse_lazy("todo-list:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    queryset = Task.objects.prefetch_related("tags")
    form_class = TaskForm
    success_url = reverse_lazy("todo-list:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo-list:index")


class SwitchAssignmentIsDoneOrNot(generic.View):

    @staticmethod
    def get(request, pk):
        task_filter = Task.objects.filter(pk=pk)
        task_get = Task.objects.get(pk=pk)
        task_filter.update(done_or_not=False) if task_get.done_or_not else task_filter.update(done_or_not=True)

        return HttpResponseRedirect(reverse_lazy("todo-list:index"))


class TagsListView(generic.ListView):
    model = Tags


class TagsCreateView(generic.CreateView):
    model = Task
    form_class = TagsForm
    success_url = reverse_lazy("todo-list:tags-list")


class TagsUpdateView(generic.UpdateView):
    model = Tags
    form_class = TagsForm
    success_url = reverse_lazy("todo-list:tags-list")


class TagsDeleteView(generic.DeleteView):
    model = Tags
    success_url = reverse_lazy("todo-list:tags-list")
