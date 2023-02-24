from django.urls import path,include,re_path


from .views import  Login,Registers


urlpatterns = [
    # path('admin/', admin.site.urls),
    # re_path('^',include(('users.urls','users'),namespace='users')),
    re_path('^user/login/$',Login.as_view(),name='login'),
    re_path('^user/register/$',Registers.as_view(),name='register')

]