# Generated by Django 4.2.2 on 2023-06-23 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_options_alter_profile_table_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='user/'),
        ),
    ]