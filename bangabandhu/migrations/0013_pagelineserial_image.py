# Generated by Django 4.2.2 on 2023-07-10 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bangabandhu', '0012_audiobook_total_pages'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagelineserial',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='line_image'),
        ),
    ]
