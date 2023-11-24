from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserAccount(User):
    pass

    def __str__(self):
        return f"{self.id} - {self.username}"

class UserProfile(models.Model):
    user_account = models.OneToOneField(UserAccount, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user_account.last_name}, {self.user_account.first_name}"
