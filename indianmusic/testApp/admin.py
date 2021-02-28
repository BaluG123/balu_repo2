from django.contrib import admin
from testApp.models import Music,Video

class MusicAdmin(admin.ModelAdmin):
    list_display=['artistimage','artistname','song','songname','duration','uploaded']
    list_filter=('artistname','songname','duration')
    date_hierarchy='uploaded'
    searchfields=('songname','artistname')

class VideoAdmin(admin.ModelAdmin):
    list_display=['video','title','image','uploaded']
    list_filter=('title','uploaded')

# Register your models here.
admin.site.register(Music,MusicAdmin)
admin.site.register(Video,VideoAdmin)
