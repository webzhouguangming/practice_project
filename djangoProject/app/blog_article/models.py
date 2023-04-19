from django.db import models
from django.urls import reverse
# 富文本编辑器模块
from ckeditor_uploader.fields import RichTextUploadingField
# 用这个函数截取字段中的字符串
from django.utils.html import strip_tags
from django.contrib.auth.models import AbstractUser
# Create your models here.


# 文章作者
class ArticleAuthor(AbstractUser):
    nickname = models.CharField(max_length=256, verbose_name='昵称', blank=True, null=True)
    phone = models.CharField(max_length=11, verbose_name='手机号', blank=True, null=True)
    # 后期需要修改。用户上传头像的路径
    head_img = models.ImageField(upload_to='app', blank=True, null=True, verbose_name='用户头像')

    def __str__(self):
        return self.username

    class Meta:
        db_table = 't_article_author'
        verbose_name = '文章作者'
        verbose_name_plural = verbose_name


# 文章类别
class Category(models.Model):

    name = models.CharField(max_length=256, verbose_name='分类名')
    des = models.CharField(max_length=256, verbose_name='备注', null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 't_category'
        verbose_name = '分类名'
        verbose_name_plural = verbose_name


# 文章标签
class Tag(models.Model):

    name = models.CharField(max_length=256, verbose_name='标签名')
    des = models.CharField(max_length=256, verbose_name='备注', null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 't_tag'
        verbose_name = '标签名'
        verbose_name_plural = verbose_name


# 文章内容
class BlogArticle(models.Model):
    # 文章标题
    title = models.CharField(max_length=70, verbose_name='文章标题')
    body = RichTextUploadingField(verbose_name='文本字段')
    # 文章的创建时间
    create_time = models.DateTimeField(verbose_name='创建时间')
    # 文章的最后一次修改时间
    modify_time = models.DateTimeField(verbose_name='文章最后修改时间')
    excerpt = models.CharField(max_length=256, blank=True, null=True, verbose_name='文章摘要')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='分类')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='标签')
    author = models.ForeignKey(ArticleAuthor, on_delete=models.CASCADE, verbose_name='作者')
    views = models.IntegerField(default=0, verbose_name='查看次数')

    def get_absolute_url(self):
        return reverse('blog_article:detail', kwargs={'pk': self.pk})

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def save(self, *args, **kwargs):
        # 如果没有填写文章的摘要内容
        if not self.excerpt:
            self.excerpt = strip_tags(self.body)[:118]
            # 调用父类的save方法保存到数据库中
            super(BlogArticle, self).save(*args, **kwargs)
        else:
            super(BlogArticle, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-create_time']
        verbose_name = '文档管理表'
        verbose_name_plural = verbose_name






