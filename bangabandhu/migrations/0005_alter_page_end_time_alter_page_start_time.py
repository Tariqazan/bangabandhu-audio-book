# Generated by Django 4.2.2 on 2023-06-21 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bangabandhu', '0004_pageaudio_audio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='end_time',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='start_time',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
