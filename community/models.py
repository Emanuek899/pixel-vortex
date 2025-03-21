from django.db import models
from polls.models import Genre
from django.utils.translation import gettext_lazy as _
from members.models import CustomUser


# Create your models here.
class Community(models.Model):
    community_id = models.BigAutoField(
        primary_key=True)
    community_grid = models.ImageField(
        upload_to="community/communities_grids/")
    community_name = models.CharField(
        max_length=30, null=False, blank=False)
    description = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    users = models.ManyToManyField(
        CustomUser,
        related_name="community_users",
        blank=True)
    users_count = models.IntegerField(default=0)
    creation_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        choices=[("A", "Active"), ("I", "Inactive")],
        max_length=20)
    category = models.ForeignKey(
        Genre,
        related_name="categories",
        on_delete=models.SET_NULL,
        null=True,
        blank=True)

    class Meta:
        verbose_name = _("Community")
        verbose_name_plural = _("Communities")

    def __str__(self):
        users = [u.username for u in self.users.all()]
        return self.community_name


class Comment(models.Model):
    comment_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(
        "members.CustomUser",
        related_name="users_comments",
        on_delete=models.CASCADE)
    text = models.CharField(max_length=100, null=False, blank=False)
    likes_account = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

    def __str__(self):
        return self.user.username if self.user else "No user selected"


class Like(models.Model):
    like_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey("members.CustomUser", on_delete=models.CASCADE)
    post = models.ForeignKey(
        "Post",
        related_name="likes",
        on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user", "post")

    def __str__(self):
        user = self.user.username
        post = self.post.post_title
        return "Post title: [{}], liked by: [{}]".format(post, user)


class Post(models.Model):
    post_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(
        "members.CustomUser",
        related_name="users_posts",
        on_delete=models.CASCADE)
    community = models.ForeignKey(
        Community,
        related_name="posts",
        on_delete=models.CASCADE)
    post_title = models.CharField(max_length=20, null=False, blank=False)
    post_description = models.CharField(
        max_length=100,
        null=False,
        blank=False)
    post_date = models.DateTimeField(auto_now_add=True)
    likes_count = models.PositiveIntegerField(default=0)
    comments = models.ManyToManyField(
        Comment,
        related_name="comments",
        blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return "Post title: [{}], created at: [{}]".format(
            self.post_title, self.created_at)
