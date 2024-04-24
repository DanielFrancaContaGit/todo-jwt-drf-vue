from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Todo(models.Model):
    content = models.TextField(max_length=2000)
    completed = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
