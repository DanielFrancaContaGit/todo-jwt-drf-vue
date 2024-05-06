from rest_framework import generics, permissions
from .models import Todo
from .serializers import TodoSerializer

# Create your views here.


class ListCreateTodoView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = TodoSerializer

    def get_queryset(self):
        if(self.kwargs != {}):
            owner_id = self.kwargs["pk"]
            todo = Todo.objects.filter(owner=owner_id)
            return todo
        else:
            return Todo.objects.all()    


class RetriveUpdateDestroyTodoview(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = TodoSerializer

    def get_queryset(self):
        todo_id = self.kwargs["pk"]
        todo = Todo.objects.filter(id=todo_id)
        return todo
