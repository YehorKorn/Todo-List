from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todo_list.forms import TaskForm, TagsForm
from todo_list.models import Task, Tags


def index(request):
    """View function for the home page of the site."""

    task_list = Task.objects.all().prefetch_related("tags")

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "task_list": task_list,
        "num_visits": num_visits + 1,
    }

    return render(request, "todo_list/index.html", context=context)


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


def switch_assignment_is_done_or_not(request, pk):
    task_filter = Task.objects.filter(pk=pk)
    task_get = Task.objects.get(pk=pk)
    return (
        HttpResponseRedirect(reverse_lazy("todo-list:index"))
        and task_filter.update(done_or_not=False)
        if task_get.done_or_not
        else task_filter.update(done_or_not=True)
    )


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
