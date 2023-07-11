from django.shortcuts import render
from django.http import HttpResponse

from .models import Post
# Create your views here.

def home(request):
    return HttpResponse("<h1>home page</h1>")

def index(request):
    return HttpResponse("<h2>index page</h2>")

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts':posts})