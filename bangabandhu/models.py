from django.db import models
from user.models import User

# Create your models here.


class Language(models.Model):
    name = models.CharField(max_length=48, blank=True, null=True)
    icon = models.ImageField(upload_to='icon/', blank=True, null=True)

    class Meta:
        db_table = 'Language'

    def __str__(self) -> str:
        return self.name


class AudioBook(models.Model):
    name = models.CharField(max_length=248, blank=True, null=True)
    language = models.ForeignKey(
        Language, related_name='audio_book_languages', on_delete=models.CASCADE, blank=True, null=True)
    translated_name = models.CharField(max_length=48, blank=True, null=True)
    cover_image = models.ImageField(
        upload_to='cover_image/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'AudioBook'

    def __str__(self) -> str:
        return self.name


class BookContent(models.Model):
    audio_book = models.ForeignKey(
        AudioBook, related_name='audio_book_contents', on_delete=models.CASCADE, blank=True, null=True)
    content = models.CharField(max_length=500, blank=True, null=True)
    start_page = models.PositiveBigIntegerField(blank=True, null=True)
    end_page = models.PositiveBigIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'BookContent'

    def __str__(self) -> str:
        return f'{self.content}-{self.audio_book.name}-{self.audio_book.language.name}'


class Page(models.Model):
    audio_book = models.ForeignKey(
        AudioBook, on_delete=models.CASCADE, related_name='audio_book_pages', blank=True, null=True)
    chapter = models.ForeignKey(
        BookContent, on_delete=models.CASCADE, blank=True, null=True)
    page_number = models.IntegerField(blank=True, null=True)
    line_serial = models.IntegerField(blank=True, null=True)
    paragraph_count = models.IntegerField(blank=True, null=True)
    sentence_count = models.IntegerField(blank=True, null=True)
    word_count = models.IntegerField(blank=True, null=True)
    line_text = models.TextField(blank=True, null=True)
    is_image = models.BooleanField(default=False)
    total_page = models.IntegerField(blank=True, null=True)
    start_time = models.CharField(max_length=100, blank=True, null=True)
    end_time = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Page'

    def __str__(self) -> str:
        return f'{self.page_number}-{self.chapter.content}-{self.audio_book.name}-{self.audio_book.language.name}'


class PageAudio(models.Model):
    page = models.ForeignKey(
        Page, on_delete=models.CASCADE, related_name='page_audio', blank=True, null=True)
    voice = models.CharField(max_length=100, blank=True, null=True)
    speed = models.IntegerField(blank=True, null=True)
    audio = models.FileField(upload_to="audio", blank=True, null=True)
    audio_path = models.CharField(max_length=255, blank=True, null=True)
    audio_length = models.FloatField(blank=True, null=True)
    line_break_sleep = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'PageAudio'

    def __str__(self) -> str:
        return f'page number - {self.page.page_number} - {self.page.audio_book.language.name}'


class Bookmark(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="users_bookmark", blank=True, null=True)
    page_number = models.IntegerField(blank=True, null=True)
    paragraph = models.IntegerField(blank=True, null=True)
    sentence = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Bookmark'

    def __str__(self) -> str:
        return f'{self.page_number}-{self.user.email}'


class BookRequest(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    request_title = models.CharField(max_length=100, blank=True, null=True)
    request_body = models.TextField(blank=True, null=True)
    additional_note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'BookRequest'
