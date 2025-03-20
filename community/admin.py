from django.contrib import admin
from community.models import Comment, Community, Post, Like

# Register your models here.
admin.site.register(Community)
admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(Like)