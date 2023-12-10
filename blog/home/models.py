from django.db import models
from users.models import UserAccount
# Create your models here.
class Post(models.Model):
    owners_profile = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    date_and_time_published = models.DateTimeField(auto_now_add=True,
                                               blank=False,
                                               null=False,
                                               verbose_name="date and time published")
    post_content = models.TextField(blank=False,
                                    null=False,
                                    verbose_name="post content",
                                    max_length=5000)
    views = models.IntegerField(blank=False,
                                default=0,
                                null=False,
                                verbose_name="views")

    VISIBILITY_CHOICES = [
      ("PR", "Private"),
      ("PU", "Public"),
    ]
    visibility = models.CharField(blank=False,
                                  default="PU",
                                  null=False,
                                  verbose_name="visibility",
                                  max_length=2,
                                  choices=VISIBILITY_CHOICES)

    def __str__(self):
        return f"{self.owners_profile.username} - {self.id}"

    class Meta:
        ordering = ["-date_and_time_published"]

class Comment(models.Model):
    # owners_profile = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
    owners_profile = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date_and_time_published = models.DateField(auto_now_add=True,
                                               blank=False,
                                               null=False,
                                               verbose_name="date and time published")
    comment_content = models.TextField(blank=False,
                                       null=False,
                                       max_length=5000,
                                       verbose_name="comment content")

    def __str__(self):
        return self.comment_content[:20]

    class Meta:
        ordering = ["date_and_time_published"]