from django.contrib import admin
from .models import Post, PostRating
# Register your models here.
admin.site.register(Post)
admin.site.register(PostRating)