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
        depth = 1


class BookContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookContent
        fields = ('id', 'audio_book', 'content')
        depth = 1


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ('id', 'audio_book', 'chapter', 'page_number', 'line_serial', 'paragraph_count', 'sentence_count',
                  'word_count', 'line_text', 'is_image', 'total_page', 'start_time', 'end_time', 'created_at', 'updated_at')
        depth = 1


class PageAudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageAudio
        fields = ('id', 'page', 'voice', 'speed', 'audio_path', 'audio',
                  'audio_length', 'line_break_sleep', 'created_at', 'updated_at')


class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ('id', 'user', 'page_number', 'paragraph',
                  'sentence', 'created_at', 'updated_at')
