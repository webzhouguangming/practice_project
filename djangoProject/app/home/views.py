from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required


class Home(View):

    def get(self, request):

        return render(request, template_name="home_page/home.html")


class LoginTest(View):
    def get(self, request):
        return render(request, template_name='home_page/test.html')
