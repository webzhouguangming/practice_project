from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include
from djangoProject import settings
from .views import *

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    re_path('^add_question/$', AddQuestionViews.as_view(), name='add_question')


]
# 为了显示上传的图片，不加的话无法显示
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

