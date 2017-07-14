
#coding=utf-8

from django.shortcuts import render,redirect
from django.http import JsonResponse
from hashlib import sha1
from models import *

def register(requset):
    context = {'title': '注册'}
    return render(requset,'df_user/register.html',context)

# 注册表单提交
def register_handle(requset):
    # 获取表单数据
    post = requset.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    upwd2 = post.get('cpwd')
    umail = post.get('email')
    # 验证密码否则返回注册页
    if upwd != upwd2:
        return redirect('/user/register/')
    # 加密
    s1 = sha1()
    s1.update(upwd2)
    upwd3 = s1.hexdigest()
    # 保存到数据库
    user = userInfo()
    user.uname = uname
    user.upwd = upwd3
    user.umail = umail
    user.save()
    return redirect('/user/login/')

# 查询数据库用户名是否可用
def register_exist(requset):
    uname = requset.GET.get('uname')
    count = userInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count':count})

# 登录
def login(requset):
    uname = requset.COOKIES.get('uname','')
    context = {'title':'用户登录'}
    return render(requset,'df_user/login.html',context)

def login_handle(requset):
    post = requset.POST
    name = post.get('username')
    pwd = post.get('pwd')
    user = userInfo.objects.filter(uname=name)
    print user[0].umail
    s1 = sha1()
    s1.update(pwd)
    if s1.hexdigest() == user[0].upwd:
        return redirect('/user/info/')

    return redirect('/user/login/')

def login_exist(requset):
    return

def info(requuset):
    context = {'title': '用户中心'}
    return render(requuset,'df_user/user_center_info.html',context)

def api(requset):
    return JsonResponse({'name':'周润发'})