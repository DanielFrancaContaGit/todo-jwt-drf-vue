from django.urls import path
from .views import ListCreateTodoView, RetriveUpdateDestroyTodoview

app_name = "todo"

urlpatterns = [
    path("create/", ListCreateTodoView.as_view(), name="todo_create"),
    path("all/", ListCreateTodoView.as_view(), name="todo_list_all"),
    path("list/<int:pk>/", ListCreateTodoView.as_view(), name="todo_list"),
    path(
        "update/<int:pk>/", RetriveUpdateDestroyTodoview.as_view(), name="todo_update"
    ),
    path(
        "delete/<int:pk>/", RetriveUpdateDestroyTodoview.as_view(), name="todo_delete"
    ),
]
