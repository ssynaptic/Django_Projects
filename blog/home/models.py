from django.db import models
from users.models import UserProfile

# Create your models here.
class Post(models.Model):
    owners_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post_content = models.TextField(blank=False,
                                    null=False,
                                    verbose_name="Post Content")
    views = models.IntegerField(blank=False,
                                default=0,
                                null=False,
                                verbose_name="Views")

    def __str__(self):
        return f"{self.owners_profile.user_account.username} - {self.id}"

    class Meta:
        ordering = ["owners_profile"]
    # post_comments = models.ForeignKey("Comment", on_delete=models.CASCADE, related_name="post_comments")

class Comment(models.Model):
    owners_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_title = models.CharField(blank=False,
                             max_length=250,
                             null=False,
                             verbose_name="Title")
    comment_content = models.TextField(blank=False,
                                       max_length=5000,
                                       null=False,
                                       verbose_name="Comment Content")
    
    def __str__(self):
        return self.comment_title