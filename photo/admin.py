from django.contrib import admin
from photo.models import Album, Photo

class PhotoInLine(admin.StackedInline):
  model = Photo
  extra = 2


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
  inlines = (PhotoInLine, )
  list_display = ('id', 'name', 'description')

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'upload_dt')