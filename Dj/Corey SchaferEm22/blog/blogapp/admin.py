from django.contrib import admin
from blogapp.models import Post,Comment, Reply
# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Reply)
