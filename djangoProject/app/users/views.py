import time

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import View
from .models import User


from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
# Create your views here.

import re
import random


class Registers(View):
    _abc = []

    @staticmethod
    def code_generate():
        code = random.randint(1000,9999)
        return code

    def get(self, request):

        abc = self.code_generate()
        print(abc)
        self._abc.append(abc)
        return render(request, template_name='user/register.html')

    def post(self, request):

        code = self._abc[0]
        print(type(code))

        # 获取参数
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        qq_code = request.POST.get("qq_code", "")
        phone = request.POST.get("phone", "")
        real_name = request.POST.get("real_name", "")
        verify_code = request.POST.get("verify_code", "")
        vc = int(verify_code)

        # 验证手机号
        p = re.match(r'^1[35789]\d{9}$', phone).group()
        if p != phone:
            return JsonResponse({"code": 406, "error_msg": '手机号格式不正确'})
        # 验证用户名
        u = re.match(r'^[a-zA-Z\d-_]{6,16}$', username).group()
        if u != username:
            return JsonResponse({"code": 406, "error_msg": '用户名格式不正确'})

        # 验证验证码
        if vc != code:
            raise ValueError("验证码不正确")

        # 保存到数据库中

        User.objects.create(username=u, password=password, QQ_code=qq_code, verify_code=vc, real_name=real_name)
        # 返回响应
        return HttpResponseRedirect("/user/login")


class Login(View):

    def get(self, request):
        return render(request, template_name='user/login.html')

    def post(self, request):
        username = request.POST.get("username", "")

        if username:
            password = request.POST.get("password", "")
            u=User.objects.filter(username=username).first()
            if u.password == password:
                return HttpResponseRedirect('/home_page/home')

            else:
                raise ValueError("用户名或密码错误")

        else:
            raise ValueError("未传递用户名")





