from django.shortcuts import render
from django.views.generic.base import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from blog_article.form import AddQuestionsForm

# Create your views here.


class AddQuestionViews(View):
    def get(self, request):
        content = {}
        add_question_form = AddQuestionsForm()
        content['add_question_form'] = add_question_form
        return render(request, template_name='blog_articles/add_question.html', context=content)

    def post(self, request):
        
        add_questions_form = AddQuestionsForm(request.POST)
        if add_questions_form.is_valid():
            add_question = add_questions_form.save(commit=False)
            add_question.author = request.user
            add_question.save()
            content = {}
            content['add_questions_form'] = add_questions_form
            return render(request, 'blog_articles/add_question.html', content)




if __name__ == '__main__':
    d=dict
    print(d)