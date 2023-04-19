from django.contrib import admin

# Register your models here.

from .models import Tag, BlogArticle, ArticleAuthor, Category


class BlogArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_time', 'modify_time', 'category', 'author', 'views')


# 分别注册模型
admin.site.register(ArticleAuthor)
admin.site.register(BlogArticle, BlogArticleAdmin)
admin.site.register(Category)
admin.site.register(Tag)