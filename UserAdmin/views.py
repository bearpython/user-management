from django.shortcuts import render,HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
import os
from UserAdmin import models
from django.views import View
# Create your views here.


def orm(request):
    # models.UserAdmin.objects.create(
    #     adminname="admin",
    #     adminpassword="666",
    # )
    return HttpResponse("ORM 添加后台管理用户成功")

def login(request):
    error_msg = ""
    if request.method == "POST":
        user = request.POST.get("username",None)
        pwd = request.POST.get("password",None)
        error_msg = ""
        admin_list = models.UserAdmin.objects.all()
        #print(admin_list)
        if admin_list:
            for row in admin_list:
                if user == row.adminname and pwd == row.adminpassword:
                    #去跳转
                    # global current_admin
                    # current_admin = user
                    return redirect("/um/index")
                else:
                    error_msg = "用户名或密码错误"
        else:
            error_msg = "用户名或密码错误"
    return render(request,"login.html",{"error_msg":error_msg})


class Index(View):
    def dispatch(self, request, *args, **kwargs):
        """这个方式是父类View里的，如果在这里又定义了一个同名的方法，那就先执行当前的，但是我又想继续用原生的dispatch的功能，那就需要调用一下父类的dispatch方法
        这样在这里就类似于装饰器，可以在请求过来之后做一些处理"""
        # print("before")
        result = super(Index,self).dispatch(request, *args, **kwargs)
        #print("after")
        return result

    def get(self,request):
        # print(request.method)
        return render(request, "index.html")

    def post(self,request):
        return render(request, "index.html", {"admin_msg": admin_msg})

def welcome(request):
    user_count = models.UserInfo.objects.count()
    dept_count = models.UserGroup.objects.count()
    #print(user_count)
    return render(request, "welcome.html",{"user_count":user_count,"dept_count":dept_count})

def grouplist(request):
    group_list = models.UserGroup.objects.all()
    return render(request, "group-list.html",{'group_list':group_list})


def groupadd(request):
    if request.method == "POST":
        groupname = request.POST.get("username",None)
        groupdept = request.POST.get("groupdept",None)
        print(groupdept,groupname)
        models.UserGroup.objects.create(caption=groupname,dept=groupdept)
        return redirect("/um/group-list")
    else:
        return render(request, "group-add.html")

def groupdel(request,nid):
    models.UserGroup.objects.filter(uid=nid).delete()
    return redirect("/um/group-list")

def groupedit(request,nid):
    if request.method == "GET":
        obj = models.UserGroup.objects.filter(uid=nid).first()
        return render(request,'group-edit.html',{"obj":obj})
    elif request.method == "POST":
        group_id = request.POST.get("groupid")
        group_name = request.POST.get("groupname")
        group_dept = request.POST.get("groupdept")
        #print(group_id,group_dept,group_name)
        models.UserGroup.objects.filter(uid=group_id).update(caption=group_name,dept=group_dept)
        return redirect("/um/group-list")

def userlist(request):
    user_list = models.UserInfo.objects.all()
    return render(request, "user-list.html",{'user_list':user_list})


def usermanagement(request):
    if request.method == "POST":
        user_name = request.POST.get('username')
        user_ip = request.POST.get('ip')
        user_gender = request.POST.get('gender')
        user_email = request.POST.get('email')
        user_phone = request.POST.get('phone')
        user_testurl = request.POST.get('testurl')
        user_pwd = request.POST.get('pass')
        # print(user_name,user_dept,user_gender,user_phone,user_pwd,user_testurl)
        models.UserInfo.objects.create(username=user_name,password=user_pwd,email=user_email,testurl=user_testurl,gender=user_gender,phone=user_phone,testip=user_ip)
        return redirect("/um/user-management")
    else:
        user_list = models.UserInfo.objects.all()
        return render(request, "user-management.html",{'user_list':user_list})

def userdel(request,uid):
    models.UserInfo.objects.filter(id=uid).delete()
    return redirect("/um/user-management")

def useredit(request,uid):
    #print(uid)
    if request.method == 'GET':
        user_info= models.UserInfo.objects.filter(id=uid).first()
        #print(user_info.username)
        return render(request, "user-edit.html",{'user_info':user_info})
    else:
        user_name = request.POST.get('username')
        user_ip = request.POST.get('ip')
        user_gender = request.POST.get('gender')
        user_email = request.POST.get('email')
        user_phone = request.POST.get('phone')
        user_testurl = request.POST.get('testurl')
        user_pwd = request.POST.get('pass')
        models.UserInfo.objects.filter(id=uid).update(username=user_name,password=user_pwd,email=user_email,testurl=user_testurl,gender=user_gender,phone=user_phone,testip=user_ip)
        return redirect("/um/user-management")