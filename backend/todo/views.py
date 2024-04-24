from .models import Todo
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    DestroyAPIView,
    UpdateAPIView,
)
from .serializers import TodoSerializer
from rest_framework import permissions

# Create your views here.


class CreateTodoView(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class ListTodoView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = TodoSerializer

    def get_queryset(self):
        owner_id = self.request.data["id"]
        todo = Todo.objects.filter(owner=owner_id)

        return todo


class DeleteTodoView(DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = TodoSerializer

    def get_queryset(self):
        todo_id = self.kwargs["pk"]
        todo = Todo.objects.filter(id=todo_id)
        return todo


class UpdateTodoView(UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = TodoSerializer

    def get_queryset(self):
        todo_id = self.kwargs["pk"]
        todo = Todo.objects.filter(id=todo_id)
        return todo
