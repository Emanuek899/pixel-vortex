from django.db import models
from polls.models import Genre
from django.utils.translation import gettext_lazy as _
from django.apps import apps

# Create your models here.
class Community(models.Model):
    community_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey("members.CustomUser", related_name="users_community", on_delete=models.CASCADE)
    community_name = models.CharField(max_length=30, null=False, blank=False)
    users_count = models.IntegerField(default=0)
    creation_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=[("A", "Active"), ("I", "Inactive")], max_length=20)
    category = models.ForeignKey(Genre, related_name="categories", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name =_("Community")
        verbose_name_plural = _("Communities")

    def __str__(self):
        return self.community_name


class Comment(models.Model):
    comment_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey("members.CustomUser", related_name="users_comments", on_delete=models.CASCADE)
    text = models.CharField(max_length=100, null=False, blank=False)
    likes_account = models.PositiveIntegerField(default=0)
    

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

    def __str__(self):
        return self.user.username if self.user else "No user selected"
    

class Post(models.Model):
    post_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey("members.CustomUser", related_name="users_posts", on_delete=models.CASCADE)
    community_id = models.ForeignKey(Community, related_name="posts", on_delete=models.CASCADE)
    post_title = models.CharField(max_length=20, null=False, blank=False)
    post_description = models.CharField(max_length=100, null=False, blank=False)
    post_date = models.DateTimeField(auto_now_add=True)
    likes_count = models.PositiveIntegerField(default=0)
    comments = models.ManyToManyField(Comment, related_name="comments", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return "Post title: [{}], created at: [{}]".format(self.post_title, self.created_at)