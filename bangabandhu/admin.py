from django.contrib import admin
from .models import Language, AudioBook, PageLineSerial, PageAudio, BookContent, Bookmark, PageNumber


# Register your models here.


admin.site.register(Language)
admin.site.register(AudioBook)
admin.site.register(PageLineSerial)
admin.site.register(PageAudio)
admin.site.register(BookContent)
admin.site.register(Bookmark)
admin.site.register(PageNumber)
