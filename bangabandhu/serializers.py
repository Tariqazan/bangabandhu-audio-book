from rest_framework import serializers
from .models import Language, AudioBook, Page, PageAudio, BookContent, Bookmark


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'name', 'icon')


class AudioBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioBook
        fields = ('id', 'name', 'language', 'cover_image', 'translated_name',
                  'created_at', 'updated_at')


class BookContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookContent
        fields = ('id', 'audio_book', 'content')


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ('id', 'audio_book', 'chapter', 'page_number', 'line_serial', 'paragraph_count', 'sentence_count',
                  'word_count', 'line_text', 'is_image', 'total_page', 'start_time', 'end_time', 'created_at', 'updated_at')
