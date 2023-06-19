from django.contrib import admin
from .models import User, Group, Profile

# Register your models here.
admin.site.register(Group)
admin.site.register(User)
admin.site.register(Profile)