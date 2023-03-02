from django.db import models

# Create your models here.
from django.db import models

from django.contrib.auth.models import User

from django.utils import timezone


class User(models.Model):

    name = models.CharField(max_length=20,unique=True)

    class Meta:
        db_table = 'article_user'
        verbose_name='作者'
        verbose_name_plural=verbose_name


class ArticlePost(models.Model):

    # 文章作者
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # 文章标题
    title = models.CharField(max_length=100)

    # 文章正文。保存大量文本使用 TextField
    body = models.TextField()

    created = models.DateTimeField(default=timezone.now)

    updated = models.DateTimeField(auto_now=True)
    # 文章票数
    ticket = models.IntegerField()

    class Meta:

        # '-created' 表明数据应该以倒序排列
        ordering = ('-created',)

    def __str__(self):
        # return self.title 将文章标题返回
        return self.title


class Image(models.Model):

    name = models.CharField(max_length=50)
    url = models.CharField(max_length=255)
    format = models.CharField(max_length=20, null=True, blank=True)
    article = models.ForeignKey(ArticlePost, on_delete=models.CASCADE, related_name='image_article')

    class Meta:
        db_table = 'image'
        verbose_name = '图片'
        verbose_name_plural=verbose_name





