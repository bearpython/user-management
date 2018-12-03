from django.db import models

# Create your models here.

class UserAdmin(models.Model):
    adminname = models.CharField(max_length=32,verbose_name="用户名")
    adminpassword = models.CharField(max_length=64,help_text="input password")

class UserGroup(models.Model):
    uid = models.AutoField(primary_key=True)
    caption = models.CharField(max_length=32)
    dept = models.CharField(max_length=64,null=True)
    ctime = models.DateTimeField(auto_now_add=True,null=True)
    utime = models.DateTimeField(auto_now=True,null=True)


class UserInfo(models.Model):
    username = models.CharField(max_length=32,verbose_name="用户名")
    password = models.CharField(max_length=64,help_text="input password")
    email = models.EmailField(max_length=19,null=True)
    testurl = models.URLField(max_length=19, null=True)
    gender = models.CharField(max_length=16)
    phone = models.CharField(max_length=32,default=8868)
    testip = models.GenericIPAddressField(max_length=19, null=True)
    ctime = models.DateTimeField(auto_now_add=True,null=True)
    utime = models.DateTimeField(auto_now=True,null=True)
    user_tpye_choices = (
        (1,"超级用户"),
        (2,"普通用户"),
        (3,"开发用户"),
    )
    user_type_id = models.IntegerField(choices=user_tpye_choices,default=1)
    user_group = models.ForeignKey("UserGroup",to_field="uid",default=1)  #外键关联，现在就是user_info表里的内容与user_group表里的uid自增字段关联
