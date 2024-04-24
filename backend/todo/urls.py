from django.urls import path
from .views import CreateTodoView, ListTodoView, DeleteTodoView, UpdateTodoView

app_name = "todo"

urlpatterns = [
    path("create/", CreateTodoView.as_view(), name="todo_create"),
    path("list/", ListTodoView.as_view(), name="todo_list"),
    path("delete/<int:pk>/", DeleteTodoView.as_view(), name="todo_delete"),
    path("update/<int:pk>/", UpdateTodoView.as_view(), name="todo_update"),
]
