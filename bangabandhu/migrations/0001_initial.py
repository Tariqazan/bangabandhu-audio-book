# Generated by Django 4.2.2 on 2023-06-20 13:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AudioBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=248, null=True)),
                ('language', models.CharField(blank=True, max_length=48, null=True)),
                ('translated_name', models.CharField(blank=True, max_length=48, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'AudioBook',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_number', models.IntegerField(blank=True, null=True)),
                ('paragraph_count', models.IntegerField(blank=True, null=True)),
                ('sentence_count', models.IntegerField(blank=True, null=True)),
                ('word_count', models.IntegerField(blank=True, null=True)),
                ('texts', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('audio_book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='audio_book_pages', to='bangabandhu.audiobook')),
            ],
            options={
                'db_table': 'Page',
            },
        ),
        migrations.CreateModel(
            name='PageAudio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voice', models.CharField(blank=True, max_length=100, null=True)),
                ('speed', models.IntegerField(blank=True, null=True)),
                ('audio_path', models.CharField(blank=True, max_length=255, null=True)),
                ('audio_length', models.FloatField(blank=True, null=True)),
                ('line_break_sleep', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='page_audio', to='bangabandhu.page')),
            ],
            options={
                'db_table': 'PageAudio',
            },
        ),
        migrations.CreateModel(
            name='BookRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_title', models.CharField(blank=True, max_length=100, null=True)),
                ('request_body', models.TextField(blank=True, null=True)),
                ('additional_note', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'BookRequest',
            },
        ),
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_number', models.IntegerField(blank=True, null=True)),
                ('paragraph_id', models.IntegerField(blank=True, null=True)),
                ('sentence_id', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users_bookmark', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Bookmark',
            },
        ),
    ]
