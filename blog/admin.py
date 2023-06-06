from django.contrib import admin
from .models import Blogs
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display=('date', 'author', 'likes_counter')

admin.site.register(Blogs, BlogAdmin)
