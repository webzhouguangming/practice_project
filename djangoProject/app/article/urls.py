from django.urls import path, include, re_path
from .views import ArticleList
from . import views

urlpatterns = [


    #re_path('^user/login/$', Login.as_view(), name='login'),
    re_path('^article/$', ArticleList.as_view(), name='article'),
    # 写文章
    path('article-create/', views.article_create, name='article_create'),
    # 文章详情
    path('article-detail/<int:id>/', views.article_detail, name='article_detail'),
    path('article-ticket/', views.Ticket.as_view(), name='article_ticket'),
    re_path('^vote_show$', views.VoteShow.as_view(), name='vote_show')


]