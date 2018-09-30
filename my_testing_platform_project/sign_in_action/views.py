from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth


# Create your views here.
def sign_in(request):
    return render(request, template_name='sign_in.html')


def home(request):
    # return HttpResponse(content='账号或密码不能为空')
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # print('username:', username)
        # print('pasword:', password)
        # print('------:', type(username), type(password))
        if username == '':
            return render(request, template_name='sign_in.html', context={'error': '用户名不能为空'})
        elif password == '':
            return render(request, template_name='sign_in.html', context={'error': '密码不能为空'})
        # elif username == 'admin' and password == '123456':
        #     return render(request,template_name='home.html')
        else:
            # return render(request, template_name='sign_in.html', context={'error': '没有我的同意，你输入什么账号和密码都不能登陆'})
            user = auth.authenticate(username=username, password=password)
            print(user)
            if  user != None  :
                auth.login(request,user)
                return render(request, template_name='home.html')
            else:
                return render(request, template_name='sign_in.html', context={'error': '用户名或密码错误'})

