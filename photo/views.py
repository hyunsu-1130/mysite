from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from photo.models import Album, Photo

class AlbumLV(ListView):
  model = Album
  
  #context_object_name = 'object_list'      # context = {'object_list' : .....}
  #template_name = 'photo/album_list.html'    # ListView의 기본 템플릿명 : 앱이름/모델_list.html
  
 
  # def get_queryset(self):
    # return self.model.objects.all()
  # def get_context_data
  # def get_object  # DV

class AlbumDV(DetailView):
  model = Album
  # PK를 통해서 특정 앨범만 가져온다.


class PhotoDV(DetailView):
  model = Photo
