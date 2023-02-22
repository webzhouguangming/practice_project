from django.shortcuts import render
from django.views import View
from .models import Register


from django.http import HttpResponse,JsonResponse
# Create your views here.

import re


class Registers(View):
    def get(self,request):
        return render(request,template_name='user/register.html')
    #参数校验
    def verify_username(self,username):
        #用户名为英文字母、数字、下划线
        u=re.match( '/^ [a-zA-Z0-9-_]{6,16}$/',username).group()
        if u!=username:
            return JsonResponse({'code':406,"errormsg":'用户名格式不正确'})
        else:
            return



    #验证手机号

    def verify_phone(self, phone):
            # 用户名为英文字母、数字、下划线
            p = re.match('/^1[35789]\d{9}$/', phone).group()
            if p != phone:
                return JsonResponse({'code': 406, "errormsg": '手机号格式不正确'})
            else:
                return


    def post(self,request):

        #获取参数
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        print(username,password)
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        print(phone)
        real_name = request.POST.get('real_name', '')
        sex = request.POST.get('sex', '')
        birth_data = request.POST.get('birth_data', '')
        verify_code = request.POST.get('verify_code', '')
        #参数校验
        #验证手机号
        p = re.match('^1[35789]\d{9}$', phone).group()
        if p != phone:
            return JsonResponse({'code': 406, "errormsg": '手机号格式不正确'})
        #验证用户名
        u = re.match('^[a-zA-Z0-9-_]{6,16}$', username).group()
        if u != username:
            return JsonResponse({'code': 406, "errormsg": '用户名格式不正确'})

        #保存到数据库中

        Register.objects.create(username=u,password=password,email=email,phone=p,verify_code=verify_code,sex=sex,
                                real_name=real_name,birth_data=birth_data)
        # 返回响应
        return JsonResponse({'code':200,'errormsg':'成功保存数据'.decode('utf8')})












