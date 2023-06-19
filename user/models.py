from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # Add custom fields or methods here
    # ...

    def __str__(self):
        return self.username