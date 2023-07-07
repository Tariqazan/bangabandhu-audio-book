from django.urls import path
from .views import *

urlpatterns = [
    path('language/', LanguageListView.as_view()),
    path('language/<int:pk>/', LanguageRetrieveView.as_view()),

    path('audiobook/', AudioBookListView.as_view()),
    path('audiobook/<int:pk>/', AudioBookRetrieveView.as_view()),

    path('book/content/', BookContentListView.as_view()),
    path('book/content/<int:pk>/', BookContentRetrieveView.as_view()),

    path('page/', PageListView.as_view()),
    path('page/<int:pk>/', PageRetrieveView.as_view()),

    path('page/audio/', PageAudioListView.as_view()),
    path('page/audio/<int:pk>/', PageAudioRetrieveView.as_view()),

    path('bookmark/', BookmarkListCreateView.as_view()),
    path('bookmark/<int:pk>/', BookmarkRetrieveView.as_view()),
]
