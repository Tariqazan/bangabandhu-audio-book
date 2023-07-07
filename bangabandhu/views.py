from rest_framework import generics
from .models import Language, AudioBook, PageLineSerial, PageAudio, BookContent, Bookmark
from .serializers import LanguageSerializer, AudioBookSerializer, BookContentSerializer, PageLineSerializer, PageAudioSerializer, BookmarkSerializer

# Create your views here.


class LanguageListView(generics.ListAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class LanguageRetrieveView(generics.RetrieveAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class AudioBookListView(generics.ListAPIView):
    queryset = AudioBook.objects.all()
    serializer_class = AudioBookSerializer


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
    queryset = PageLineSerial
    serializer_class = PageLineSerializer

    def get_queryset(self):
        language_id = self.request.GET.get('lang')
        page_number = self.request.GET.get('page_number')
        chapter_name = self.request.GET.get('chapter_name')
        pages = self.queryset.objects.filter(
            page_number__audio_book__language_id=language_id, page_number__number=page_number, page_number__chapter__content=chapter_name)
        return pages


class PageRetrieveView(generics.RetrieveAPIView):
    queryset = PageLineSerial.objects.all()
    serializer_class = PageLineSerializer


class PageAudioListView(generics.ListAPIView):
    queryset = PageAudio
    serializer_class = PageAudioSerializer

    def get_queryset(self):
        language_id = self.request.GET.get('lang')
        page_number = self.request.GET.get('page_number')
        chapter_name = self.request.GET.get('chapter_name')
        page_audios = self.queryset.objects.filter(
            page_number__audio_book__language_id=language_id, page_number__number=page_number, page_number__chapter__content=chapter_name)
        return page_audios


class PageAudioRetrieveView(generics.RetrieveAPIView):
    queryset = PageAudio.objects.all()
    serializer_class = PageAudioSerializer


class BookmarkListCreateView(generics.ListCreateAPIView):
    queryset = Bookmark
    serializer_class = BookmarkSerializer

    def get_queryset(self):
        bookmarks = self.queryset.objects.filter(
            user_id=self.request.user.id)
        return bookmarks

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id,
                        page_id=self.request.data['page_id'])
        return super().perform_create(serializer)


class BookmarkRetrieveView(generics.RetrieveAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
