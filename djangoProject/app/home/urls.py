from django.contrib.auth.decorators import login_required
from django.urls import path,include,re_path


from .views import Home,LoginTest


urlpatterns = [
    # 初次访问首页 需要登陆
    re_path('^$', login_required(Home.as_view()), name='home'),
    # 登陆后重定向到首页
    re_path('^user/login/home/$', Home.as_view(), name='home'),
    re_path('^home/test$', LoginTest.as_view(), name='test')

]