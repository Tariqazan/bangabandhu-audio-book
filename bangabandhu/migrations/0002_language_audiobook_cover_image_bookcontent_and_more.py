# Generated by Django 4.2.2 on 2023-06-20 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bangabandhu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=48, null=True)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='icon/')),
            ],
            options={
                'db_table': 'Language',
            },
        ),
        migrations.AddField(
            model_name='audiobook',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='cover_image/'),
        ),
        migrations.CreateModel(
            name='BookContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(blank=True, max_length=500, null=True)),
                ('audio_book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='audio_book_contents', to='bangabandhu.audiobook')),
            ],
            options={
                'db_table': 'BookContent',
            },
        ),
        migrations.AlterField(
            model_name='audiobook',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='audio_book_languages', to='bangabandhu.language'),
        ),
    ]
