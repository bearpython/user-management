"""UM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from UserAdmin import views

urlpatterns = [
    url(r'^login', views.login),
    url(r'^index', views.Index.as_view()),  #这种是类的写法
    url(r'^orm', views.orm),
    url(r'^welcome', views.welcome),
    url(r'^group-list', views.grouplist),
    url(r'^group-add', views.groupadd),
    url(r'^groupdel-(?P<nid>\d+)', views.groupdel),
    url(r'^groupedit-(?P<nid>\d+)', views.groupedit),
    url(r'^user-list', views.userlist),
    url(r'^user-management', views.usermanagement),
    url(r'^userdel-(?P<uid>\d+)', views.userdel),
    url(r'^useredit-(?P<uid>\d+)', views.useredit),
    # url(r'^user_info/', views.user_info),
    # url(r'^userdetail-(?P<nid>\d+)', views.user_detail),
    # url(r'^userdel-(?P<nid>\d+)/', views.user_del),
    # url(r'^useredit-(?P<nid>\d+)/', views.user_edit),
    # url(r'^user_group/', views.user_group),
    # url(r'^index', views.index),
]