
from django.urls import path,include,re_path


from .views import Home


urlpatterns = [
    # path('admin/', admin.site.urls),
    # re_path('^',include(('users.urls','users'),namespace='users')),
    re_path('^home_page/home$', Home.as_view(), name='home')


]