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
    total_pages = models.CharField(max_length=248, blank=True, null=True)
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


class PageNumber(models.Model):
    audio_book = models.ForeignKey(
        AudioBook, on_delete=models.CASCADE, related_name='audio_book_pages', blank=True, null=True)
    chapter = models.ForeignKey(
        BookContent, on_delete=models.CASCADE, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'PageNumber'

    def __str__(self) -> str:
        return f'Page-{self.number}-Book Name({self.audio_book.name})'


class PageLineSerial(models.Model):
    page_number = models.ForeignKey(
        PageNumber, on_delete=models.CASCADE, blank=True, null=True)
    line_serial = models.IntegerField(blank=True, null=True)
    paragraph_count = models.IntegerField(blank=True, null=True)
    sentence_count = models.IntegerField(blank=True, null=True)
    word_count = models.IntegerField(blank=True, null=True)
    line_text = models.TextField(blank=True, null=True)
    total_page = models.IntegerField(blank=True, null=True)
    start_time = models.CharField(max_length=100, blank=True, null=True)
    end_time = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'PageLineSerial'

    def __str__(self) -> str:
        return f'Page Number - {self.page_number.number} - Book {self.page_number.audio_book.name} - Chapter {self.page_number.chapter.content} - Language {self.page_number.audio_book.language.name} - Line Serial {self.line_serial}'


class PageAudio(models.Model):
    page_number = models.ForeignKey(
        PageNumber, on_delete=models.CASCADE, related_name='page_number_audio', blank=True, null=True)
    voice = models.CharField(max_length=100, blank=True, null=True)
    speed = models.IntegerField(blank=True, null=True)
    audio = models.FileField(upload_to="audio", blank=True, null=True)
    audio_path = models.CharField(max_length=255, blank=True, null=True)
    audio_length = models.FloatField(blank=True, null=True)
    is_image = models.BooleanField(default=False)
    image = models.ImageField(blank=True, null=True, upload_to='line_image')
    line_break_sleep = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'PageAudio'

    def __str__(self) -> str:
        return f'Page Number - {self.page_number.number} - Book {self.page_number.audio_book.name} - Chapter {self.page_number.chapter.content} - Language {self.page_number.audio_book.language.name}'


class Bookmark(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="users_bookmark", blank=True, null=True)
    line_serial = models.ForeignKey(
        PageLineSerial, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Bookmark'

    def __str__(self) -> str:
        return f'{self.user.email}'


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
