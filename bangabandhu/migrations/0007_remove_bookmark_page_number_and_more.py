# Generated by Django 4.2.2 on 2023-06-28 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bangabandhu', '0006_bookcontent_end_page_bookcontent_start_page'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmark',
            name='page_number',
        ),
        migrations.RemoveField(
            model_name='bookmark',
            name='paragraph',
        ),
        migrations.RemoveField(
            model_name='bookmark',
            name='sentence',
        ),
        migrations.AddField(
            model_name='bookmark',
            name='page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bangabandhu.pageaudio'),
        ),
    ]