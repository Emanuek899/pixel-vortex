from django.contrib import admin
from community.models import PostComment, Community, Post, PostLike

# Register your models here.
admin.site.register(Community)
admin.site.register(PostComment)
admin.site.register(Post)
admin.site.register(PostLike)