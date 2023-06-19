from django.db import models


# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class GlobalSetting(BaseModel):
    favicon = models.ImageField(upload_to="favicon/", blank=True, null=True)
    primary_logo = models.ImageField(upload_to="logo/", blank=True, null=True)
    recaptcha = models.CharField(max_length=255, blank=True, null=True)
    google_analytics = models.BooleanField(default=False)
    gdpr_policy = models.BooleanField(default=False)
    facebook_url = models.CharField(max_length=2083, blank=True, null=True)
    instagram_url = models.CharField(max_length=2083, blank=True, null=True)
    twitter_url = models.CharField(max_length=2083, blank=True, null=True)
    youtube_url = models.CharField(max_length=2083, blank=True, null=True)

    class Meta:
        db_table = "GlobalSetting"


class SmtpSetting(BaseModel):
    global_setting = models.ForeignKey(
        GlobalSetting, on_delete=models.DO_NOTHING, blank=True, null=True
    )
    smtp_type = models.CharField(max_length=10, blank=True, null=True)
    email_host = models.CharField(max_length=48, blank=True, null=True)
    email_port = models.PositiveBigIntegerField(blank=True, null=True)
    email_host_user = models.CharField(max_length=48, blank=True, null=True)
    email_host_password = models.CharField(max_length=48, blank=True, null=True)
    default_from_email = models.CharField(max_length=48, blank=True, null=True)

    class Meta:
        db_table = "SmtpSetting"
