from django.db import models

# Create your models here.

# تعریف کردن یک منیجر مثل همون ابجکتس با این تفاوت که یک فیلتر بیشتر برای این منیجر گذاشتیم
class PostLiveManager(models.Manager):
    def get_queryset(self):
        queryset = super().get_queryset()
        # اضافه کردن یک فیلتر بیشتر
        queryset = queryset.filter(is_enable=False)
        return queryset

class Post(models.Model):
    #fieldName = Discriptor()
    title = models.CharField(max_length=50)
    
    #blank == true اجباری نیست میتواند خالی باشد
    # به صورت دیفالت فالس هست این مقدار و یعنی اجباری هست فیلد مربوطه
    text = models.TextField(blank=True)
    
    is_enable = models.BooleanField(default=False)
    
    # اگر بخواد نال ترو درست باشه یعنی کاربر 
    # بتونه چیزی نزنه پس نباید فیلدش اجباری باشه
    publish_date = models.DateField(null=True, blank=True)
    
    #auto_now_add بلافاصله زمان فعلی را براش ست میکنه
    created_time = models.DateField(auto_now_add=True) 
    
    #auto_now بلافاصله زمان فعلی را اپدیت میکنه
    updated_time = models.DateField(auto_now=True)

    # تعریف نام برای ابجکت های این مدل الان دیگه اگه جایی یک شی از این 
    # آبجکت بخواد نشان بده، با این فرمت به جای اینکه ابجکت طور بنویسه اوکی میکنه
    def __str__(self):
        return f'{str(self.id)}-{self.title}' 
    
    objects = models.Manager()
    live = PostLiveManager()
      
class Comment(models.Model):
    # اضافه کردن کامنت برای پست ها که خودشون مدل دارند
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    created_time = models.DateField(auto_now_add=True) 
    updated_time = models.DateField(auto_now=True)
