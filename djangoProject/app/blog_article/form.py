from django import  forms
from ckeditor.fields import RichTextFormField
from ckeditor_uploader.fields import RichTextUploadingFormField
from blog_article.models import BlogArticle


class AddQuestionsForm(forms.ModelForm):
    body = RichTextUploadingFormField(label='我是富文本编辑器', config_name='default')

    class Meta:
        model = BlogArticle
        fields = ['body']

