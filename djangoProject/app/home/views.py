from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse


class Home(View):
    def get(self, request):

        return render(request, template_name="home_page/home.html")
