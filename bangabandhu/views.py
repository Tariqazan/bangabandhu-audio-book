from rest_framework import generics
from .models import Language, AudioBook, Page, PageAudio, BookContent, Bookmark
from .serializers import LanguageSerializer, AudioBookSerializer, BookContentSerializer, PageSerializer, PageAudioSerializer, BookmarkSerializer

# Create your views here.


class LanguageListView(generics.ListAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class LanguageRetrieveView(generics.RetrieveAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class AudioBookListView(generics.ListAPIView):
    queryset = AudioBook
    serializer_class = AudioBookSerializer

    def get_queryset(self):
        language_id = self.request.GET.get('lang')
        audio_books = self.queryset.objects.filter(
            language_id=language_id)
        return audio_books


class AudioBookRetrieveView(generics.RetrieveAPIView):
    queryset = AudioBook.objects.all()
    serializer_class = AudioBookSerializer


class BookContentListView(generics.ListAPIView):
    queryset = BookContent
    serializer_class = BookContentSerializer

    def get_queryset(self):
        language_id = self.request.GET.get('lang')
        book_contents = self.queryset.objects.filter(
            audio_book__language_id=language_id)
        return book_contents


class BookContentRetrieveView(generics.RetrieveAPIView):
    queryset = BookContent.objects.all()
    serializer_class = BookContentSerializer


class PageListView(generics.ListAPIView):
    queryset = Page
    serializer_class = PageSerializer

    def get_queryset(self):
        language_id = self.request.GET.get('lang')
        pages = self.queryset.objects.filter(
            audio_book__language_id=language_id)
        return pages


class PageRetrieveView(generics.RetrieveAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer


class PageAudioListView(generics.ListAPIView):
    queryset = PageAudio
    serializer_class = PageAudioSerializer

    def get_queryset(self):
        language_id = self.request.GET.get('lang')
        page_audios = self.queryset.objects.filter(
            page__audio_book__language_id=language_id)
        return page_audios


class PageAudioRetrieveView(generics.RetrieveAPIView):
    queryset = PageAudio.objects.all()
    serializer_class = PageAudioSerializer


class BookmarkListView(generics.ListAPIView):
    queryset = Bookmark
    serializer_class = BookmarkSerializer

    def get_queryset(self):
        bookmarks = self.queryset.objects.filter(
            user_id=self.request.user.id)
        return bookmarks


class BookmarkRetrieveView(generics.RetrieveAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
