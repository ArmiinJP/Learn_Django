from django.contrib import admin
from .models import Post, Comment

# Register your models here.

# اضافه کردن مدل کامنت به مدلی که بهش ارتباط داره در صفحه ادمین
class CommentAdminInline(admin.TabularInline):
    # نحوه‌ی اتصال به مدل در شکل اینلاین به این صورته
    model = Comment
    
    # فیلدهایی که میخوای بزاری که طرف پر کنه
    fields = ['text']
    
    # برای اینکه تعداد خالی زیاد نشان نده
    extra = 0 

# نمایش فیلدهایی که میخوای در صفحه‌ی ادمین مربوط به مدل  مورد نظر
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_enable', 'publish_date', 'created_time', 'updated_time']
    inlines = [CommentAdminInline]

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'text', 'created_time', 'updated_time']

    
# اضافه کردن مدل به ادمین پنل
# در این حالت از مدل خودش استفاده میکنه که فیلدها بالا توش نیست
#admin.site.register(Post)

# اضافه کردن مدل به ادمین پنل
# به شکل کلاسی که من تعریفش کردم یعنی با فیلدهای بالا
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

# نحوه ی دیگر تعریف ادمین مدل و اضافه کردن به اون
# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ['id', 'title', 'is_enable', 'publish_date', 'created_time', 'updated_time']
#     inlines = [CommentAdminInline]
