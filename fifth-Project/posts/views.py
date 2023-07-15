from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.views import generic

from .models import Post, Comment
from .forms import PostForm

from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

def home(request):
    return HttpResponse("<h1>home page</h1>")

@api_view(['GET', 'Post'])
def index(request):
    if request.method == 'POST':
        return Response(request.data)   
    else:
        return Response({"reponse": "chetory dashi"}) 
    

# الان کلاس بیسد تعریف کردم سه تا مقدار پایین را بهش توجه کن کوئری که میزنی، تمپلیتی که میخوای رندر کنی، و کلیدهای دیکشنری که پاس میدی
# جایگزین فانکشن پایینی شد این کلاس
class Plist(generic.ListView):
    queryset = Post.objects.all()
    template_name = 'posts/list.html'
    context_object_name = 'posts'

# def plist(request):
#     posts = Post.objects.all()
#     context = {'posts' : posts}
#     return render(request, 'posts/list.html', context=context)

class Pdetail(generic.DetailView):
    model = Post
    template_name = 'posts/detail.html'
    #context_object_name = 'post'

# دو تا فانکشن خیلی عجیب که سعادت دنیا در فهمیدن کیوردآرگ هست که چی توشه که با پرینت اوکی میتونی کنی
    # def get_queryset(self):
    #     print(kwargs)
    #     return get_object_or_404(Post, id=self.kwargs["pk"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #print(kwargs)
        context["comments"] = Comment.objects.filter(post=kwargs["object"].pk)
        return context        
    
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
            # شکل فرستان کلین دیتا جذابه در این حالت
            Post.objects.create(**form.cleaned_data)
            return redirect('/list')
        else:
            return redirect('/list')
    else:
        form = PostForm()
        context = {'form' : form}
    return render(request, 'posts/create.html', context=context)