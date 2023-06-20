from rest_framework import generics
from .models import Language, AudioBook, BookContent, Page
from .serializers import LanguageSerializer, AudioBookSerializer, BookContentSerializer, PageSerializer

# Create your views here.


class LanguageListCreateView(generics.ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class LanguageRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class AudioBookListCreateView(generics.ListCreateAPIView):
    queryset = AudioBook.objects.all()
    serializer_class = AudioBookSerializer


class AudioBookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AudioBook.objects.all()
    serializer_class = AudioBookSerializer


class BookContentListCreateView(generics.ListCreateAPIView):
    queryset = BookContent.objects.all()
    serializer_class = BookContentSerializer


class BookContentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookContent.objects.all()
    serializer_class = BookContentSerializer


class PageListCreateView(generics.ListCreateAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer


class PageRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
