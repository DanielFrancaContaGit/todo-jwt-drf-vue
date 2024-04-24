from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView, ListAPIView
from .serializers import UserCreationSerializer
from rest_framework import permissions


class CreateUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreationSerializer


class ListUserView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserCreationSerializer
