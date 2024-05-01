from django.contrib import admin
from .models import Author, Post, Category, Tag, Comment, HappyClients, ContactInfo

# Register your models here.
admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(HappyClients)
admin.site.register(ContactInfo)
