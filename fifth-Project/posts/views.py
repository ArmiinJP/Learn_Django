from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound

from .models import Post, Comment
from .forms import PostForm
# Create your views here.

def home(request):
    return HttpResponse("<h1>home page</h1>")

def index(request):
    return HttpResponse("<h2>index page</h2>")

def plist(request):
    posts = Post.objects.all()
    context = {'posts' : posts}
    return render(request, 'posts/list.html', context=context)

def pdetail(request, post_id):
    # برای مدیریت کردن دیتاهایی که وجود ندارند
    # اگر نباشد خطای 500 برمیگرده اما با این کار خطای 404  برمیگرده
    # try:
    #     post = Post.objects.get(id=post_id)
    # except Post.DoesNotExist:
    #     return HttpResponseNotFound("data does not exist")

    # روش دوم مدیریت کردن خطای نبودن دیتا در دیتابیس
    post = get_object_or_404(Post, id=post_id)
    
    # اگر هم کلا دیتا را نخوای مدیریت کنی و بخوای ۵۰۰ برگرده که دیگه فبها
    #post = Post.objects.get(id=post_id)
    
    comments = Comment.objects.filter(post=post)
    context = {
        'post': post,
        'comments': comments,
    }
    return render(request, 'posts/detail.html', context=context)
    
def pcreate(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            #jazab
            Post.objects.create(**form.cleaned_data)
            return redirect('/list')
        else:
            return redirect('/list')
    else:
        form = PostForm()
        context = {'form' : form}
    return render(request, 'posts/create.html', context=context)