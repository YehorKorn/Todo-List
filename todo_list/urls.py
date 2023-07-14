from django.urls import path

from todo_list.views import (
    index,
    TaskCreateView,
    TaskUpdateView,
    switch_assignment_is_done_or_not,
    TagsListView,
    TaskDeleteView,
    TagsCreateView,
    TagsUpdateView,
    TagsDeleteView,
)

urlpatterns = [
    path('', index, name="index"),
    path('create/', TaskCreateView.as_view(), name="create"),
    path('update/<int:pk>/', TaskUpdateView.as_view(), name="update"),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name="delete"),
    path(
        "task/<int:pk>/switch_assignment/",
        switch_assignment_is_done_or_not,
        name="switch_assignment",
    ),
    path('tags/', TagsListView.as_view(), name="tags-list"),
    path('tags/create/', TagsCreateView.as_view(), name="tags-create"),
    path('tags/update/<int:pk>/', TagsUpdateView.as_view(), name="tags-update"),
    path('tags/delete/<int:pk>/', TagsDeleteView.as_view(), name="tags-delete"),
]

app_name = "todo-list"
