from rest_framework.generics import CreateAPIView, ListAPIView
from django.contrib.auth.models import User
from .serializers import UserSerializers
from rest_framework import permissions


class CreateUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class ListUserView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializers
