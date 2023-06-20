from django.urls import path
from .views import *

urlpatterns = [
    path('language/', LanguageListCreateView.as_view()),
    path('language/<int:pk>/', LanguageRetrieveUpdateDestroyView.as_view()),

    path('audiobook/', AudioBookListCreateView.as_view()),
    path('audiobook/<int:pk>/', AudioBookRetrieveUpdateDestroyView.as_view()),

    path('book/content/', BookContentListCreateView.as_view()),
    path('book/content/<int:pk>/', BookContentRetrieveUpdateDestroyView.as_view()),

    path('page/', PageListCreateView.as_view()),
    path('page/<int:pk>/', PageRetrieveUpdateDestroyView.as_view()),
]
