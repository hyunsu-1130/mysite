from django.shortcuts import render
from django.views.generic import ListView, DeleteView, DetailView
from bookmark.models import Bookmark
# Create your views here.

class BookmarkLV(ListView):
    model=Bookmark

    # template_name="bookmark/bookmark_list.html" #appname/model_name_list.html
    # context_object_name = "object_list" # object_list

class BookmarkDV(DetailView):
    model=Bookmark
    
    #template_name = 'bookmark/bookmark_detail.html'          # 사용할 템플릿 파일
    #context_object_name = 'object'            # 템플릿에서 사용할 객체의 이름

     # template_name="bookmark/bookmark_detail.html" #appname/model_name_detail.html
    # context_object_name = "object" # object
