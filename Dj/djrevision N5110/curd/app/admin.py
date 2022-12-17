from django.contrib import admin
from app.models import Book,Tag,Author
# Register your models here.

admin.site.register(Book)
admin.site.register(Tag)
admin.site.register(Author)