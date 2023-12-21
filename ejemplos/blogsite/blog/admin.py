from django.contrib import admin
from .models import Post, Category, Hashtag

# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Hashtag)
