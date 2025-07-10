from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)  # Admin/instructor
    is_student = models.BooleanField(default=True)  # Regular user

    def __str__(self):
        return self.username
