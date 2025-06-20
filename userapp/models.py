from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    profile_image = models.ImageField(upload_to='uploads/', null=True, blank=True)

    def __str__(self):
        return self.username