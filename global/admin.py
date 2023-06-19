from django.contrib import admin
from .models import GlobalSetting, SmtpSetting

# Register your models here.
admin.site.register(GlobalSetting)
admin.site.register(SmtpSetting)
