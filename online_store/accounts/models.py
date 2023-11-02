from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id} - {self.username}"

class PhoneNumber(models.Model):
    USA = "+1"
    CO = "+57"
    PREFIX_CHOICES = [
        (USA, "United States"),
        (CO, "Colombia"),
    ]

    country = models.CharField(max_length=3,
                               choices=PREFIX_CHOICES,
                               default=CO)
    phone_number = models.CharField(max_length=30)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.country} {self.phone_number}"