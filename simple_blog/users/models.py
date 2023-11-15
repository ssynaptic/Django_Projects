from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.
class UserAccount(AbstractBaseUser):
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    username = models.CharField(max_length=50, blank=False, null=False)
    password = models.CharField(max_length=256, blank=False, null=False)

    def __str__(self):
        return f"{self.id} - {self.username}"

class UserProfile(models.Model):
    account = models.OneToOneField(UserAccount, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} - {self.account.username}"