from rest_framework import serializers
from .models import Language, AudioBook, PageLineSerial, PageAudio, BookContent, Bookmark


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
        fields = ('id', 'audio_book', 'content', 'start_page', 'end_page')
        depth = 1


class PageLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageLineSerial
        fields = ('id', 'page_number', 'line_serial', 'paragraph_count', 'sentence_count',
                  'word_count', 'line_text', 'is_image', 'total_page', 'start_time', 'end_time', 'created_at', 'updated_at')
        depth = 1


class PageAudioSerializer(serializers.ModelSerializer):

    class Meta:
        model = PageAudio
        fields = ('id', 'page_number', 'voice', 'speed', 'audio_path', 'audio',
                  'audio_length', 'line_break_sleep', 'created_at', 'updated_at')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        page_lines = PageLineSerial.objects.filter(
            page_number=instance.page_number)
        page_line_data = PageLineSerializer(page_lines, many=True)
        representation['page_lines'] = page_line_data.data
        print(representation)
        return representation


class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ('id', 'user', 'page', 'created_at', 'updated_at')
