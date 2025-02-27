from django.contrib import admin
from community.models import Comment, Community, Post

# Register your models here.
admin.site.register(Community)
admin.site.register(Comment)
admin.site.register(Post)