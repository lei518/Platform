from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    contact_number = models.CharField(max_length=15)
    is_active = models.BooleanField(default=False)  # Admin must activate

class Post(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:50]  # Return a snippet of the content
