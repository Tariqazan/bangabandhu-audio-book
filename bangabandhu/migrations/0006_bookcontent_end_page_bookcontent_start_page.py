# Generated by Django 4.2.2 on 2023-06-21 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bangabandhu', '0005_alter_page_end_time_alter_page_start_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookcontent',
            name='end_page',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bookcontent',
            name='start_page',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
    ]
