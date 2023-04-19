from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.


from django.shortcuts import render

from .models import ArticlePost, User
from django.views import View


class ArticleList(View):

    def get(self, request):
        # 取出所有文章
        articles = ArticlePost.objects.all()
        # 需要传递给模板的对象
        context = {'articles': articles}
        return render(request, 'articles/list.html', context)


def article_create(request):
    if request.method == 'POST':
        new_article_title = request.POST.get('title')
        new_article_body = request.POST.get('body')
        new_article_author = User.objects.get(id=1)
        ArticlePost.objects.create(title=new_article_title, body=new_article_body,author=new_article_author)
        return redirect("article:article_list")
    # 如果用户请求获取数据
    else:
        return render(request, 'articles/create.html')

# 文章详情


def article_detail(request, id):
    # 取出相应的文章
    article = ArticlePost.objects.get(id=id)

    # 需要传递给模板的对象
    context = {'article': article}
    # 载入模板，并返回context对象
    return render(request, 'articles/detail.html', context)


class Ticket(View):

    def post(self, request):
        title = request.POST.get("title", "")
        ticket = request.POST.get("ticket", "")
        t = ArticlePost.objects.filter(title=title).first()
        t_old = t.ticket
        t_new = t_old+int(ticket)
        ArticlePost.objects.filter(id=t.id).update(ticket=t_new)
        return '成功创建'


class VoteShow(View):
    def get(self, request):
        articles = ArticlePost.objects.all()

        context = {'articles': articles}
        return render(request, template_name='articles/vote.html',context=context)