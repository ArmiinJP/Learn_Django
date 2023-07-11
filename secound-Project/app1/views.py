from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Person

# Create your views here.

def func_app1(request):
    all = Person.objects.all
    return render(request, 'test.html',{'test': all})
