from django.db import models

# Create your models here.


class Todo(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    deadline = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    