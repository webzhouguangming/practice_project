from django.contrib.auth.decorators import login_required
from django.urls import path,include,re_path



from .views import Home,LoginTest,Index


urlpatterns = [

    re_path('^$', Index.as_view(), name='home'),
    # 登陆后重定向到首页
    re_path('^user/login/home/$', Index.as_view(), name='home'),
    re_path('^home/test$', Index.as_view(), name='test')


]