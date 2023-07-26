from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=24)

    class Meta:
        db_table = "Group"


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    role = models.ForeignKey(
        Group, on_delete=models.DO_NOTHING, blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True, unique=True)
    profile_pic = models.ImageField(upload_to="user/", blank=True, null=True)
    date_of_birth = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        db_table = "User"


class Profile(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=48, blank=True, null=True)
    last_name = models.CharField(max_length=48, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    profession = models.CharField(max_length=64, blank=True, null=True)
    gender = models.CharField(max_length=24, blank=True, null=True)
    language = models.CharField(max_length=48, blank=True, null=True)
    country = models.CharField(max_length=128, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Profile"


class UserRole(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "UserRole"
