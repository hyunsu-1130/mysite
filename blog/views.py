from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, TodayArchiveView
from django.conf import settings
from blog.models import Post

from django.views.generic import FormView
from blog.forms import PostSearchForm
from django.db.models import Q

class PostLV(ListView):
  model = Post
  template_name = 'blog/post_all.html'      # blog/post_list.html
  context_object_name = 'posts'         # 템플릿 파일로 넘겨주는 객체 리스트에 대한 컨텍스트 변수명
  paginate_by = 2                       # 한 페이지에 보여주는 객체 리스트 수


class PostDV(DetailView):
  model = Post
  template_name = 'blog/post_detail.html'

  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['disqus_short'] = f"{settings.DISQUS_SHORTNAME}"
        context['disqus_id'] = f"post-{self.object.id}-{self.object.slug}"
        context['disqus_url'] = f"{settings.DISQUS_MY_DOMAIN}{self.object.get_absolute_url()}"
        context['disqus_title'] = f"{self.object.slug}"
        return context  



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


class TagCloudTV(TemplateView):
    template_name="taggit/taggit_cloud.html"

class TaggedObjectLV(ListView):
    template_name='taggit/taggit_post_list.html'
    model = Post
    def get_queryset(self):
        return Post.objects.filter(tags__name=self.kwargs.get('tag'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return context
    

class SearchFormView(FormView):
   form_class = PostSearchForm
   template_name = 'blog/post_search.html'

   def form_valid(self, form):
      # 검색어 확인
      searchWord = form.cleaned_data['search_word']

      # Q를 통해 검색
      post_list = Post.objects.filter(Q(title__icontains=searchWord) | Q(description__icontains=searchWord) | Q(content__icontains=searchWord)).distinct()
      
      # 결과를 담아
      context = {}
      context['form'] = form
      context['search_term'] = searchWord
      context['object_list'] = post_list

      # 페이지에 전달
      return render(self.request, self.template_name, context)
   