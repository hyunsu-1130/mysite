from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, TodayArchiveView

from blog.models import Post

class PostLV(ListView):
  model = Post
  template_name = 'blog/post_all.html'      # blog/post_list.html
  context_object_name = 'posts'         # 템플릿 파일로 넘겨주는 객체 리스트에 대한 컨텍스트 변수명
  paginate_by = 2                       # 한 페이지에 보여주는 객체 리스트 수


class PostDV(DetailView):
  model = Post
  template_name = 'blog/post_detail.html'



# Archive
class PostAV(ArchiveIndexView):
  model = Post
  date_field = 'modify_dt'
  template_name = 'blog/post_archive.html'

class PostYAV(YearArchiveView):
  model = Post
  date_field = 'modify_dt'
  make_object_list = True         # 해당 연도에 해당하는 객체 리스트 생성 속성
  template_name = 'blog/post_archive_year.html'

class PostMAV(MonthArchiveView):
  model = Post
  date_field = 'modify_dt'
  template_name = 'blog/post_archive_month.html'

class PostDAV(DayArchiveView):
  model = Post
  date_field = 'modify_dt'
  template_name = 'blog/post_archive_day.html'

class PostTAV(TodayArchiveView):
  model = Post
  date_field = 'modify_dt'
  template_name = 'blog/post_archive_day.html'