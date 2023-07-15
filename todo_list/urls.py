from django.urls import path

from todo_list.views import (
    TaskList,
    TaskCreateView,
    TaskUpdateView,
    SwitchAssignmentIsDoneOrNot,
    TagsListView,
    TaskDeleteView,
    TagsCreateView,
    TagsUpdateView,
    TagsDeleteView,
)

urlpatterns = [
    path("", TaskList.as_view(), name="index"),
    path("create/", TaskCreateView.as_view(), name="create"),
    path("update/<int:pk>/", TaskUpdateView.as_view(), name="update"),
    path("delete/<int:pk>/", TaskDeleteView.as_view(), name="delete"),
    path(
        "task/<int:pk>/switch_assignment/",
        SwitchAssignmentIsDoneOrNot.as_view(),
        name="switch_assignment",
    ),
    path("tags/", TagsListView.as_view(), name="tags-list"),
    path("tags/create/", TagsCreateView.as_view(), name="tags-create"),
    path("tags/update/<int:pk>/", TagsUpdateView.as_view(), name="tags-update"),
    path("tags/delete/<int:pk>/", TagsDeleteView.as_view(), name="tags-delete"),
]

app_name = "todo-list"
