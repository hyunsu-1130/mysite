from django.db import models
from django.urls import reverse

# id, title, slug, description, content, create_dt, modift_dt

class Post(models.Model):
    title = models.CharField(verbose_name='TITLE', max_length=50)
    slug = models.SlugField(verbose_name="SLUG", unique=True, allow_unicode=True, help_text="one word for title alias.")
    description = models.CharField("DESCRIPTION", max_length=100, blank=True, help_text="simple text")
    content = models.TextField("CONTENT")
    create_dt = models.DateTimeField("CREATE DATE", auto_now_add=True)
    modify_dt = models.DateTimeField("MODIFY DATE", auto_now=True)



    #  Meta 클래스는 모델의 메타데이터를 정의하는 데 사용
    class Meta:
        verbose_name = 'post'             # 모델의 단수형
        verbose_name_plural = 'posts'    # 모델의 복수형
        db_table = 'blog_posts'         # 데이터베이스에서 테이블 이름을 지정
        ordering=('-modify_dt',)        # 최근 수정순으로 내림차순
    def str(self):
        return self.title
    def get_absolute_url(self):           
        return reverse('blog:post_detail', args=(self.slug, ))
    def get_previous(self):
        return self.get_previous_by_modify_dt()
    def get_next(self):
        return self.get_next_by_modify_dt()