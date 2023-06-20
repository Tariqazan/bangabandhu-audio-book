from django.contrib import admin
from .models import Language, AudioBook, Page, PageAudio, BookContent, Bookmark


# Register your models here.


admin.site.register(Language)
admin.site.register(AudioBook)
admin.site.register(Page)
admin.site.register(PageAudio)
admin.site.register(BookContent)
admin.site.register(Bookmark)
