from django.db import models

# Create your models here.

class Person(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(auto_now=False, auto_now_add=False)
    
class Animal(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField()
    created = models.DateTimeField(auto_now=False, auto_now_add=False)    