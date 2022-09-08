from django.db import models

# Create your models here.
class AppsInfo(models.Model):
    name=models.CharField(max_length=200)
    package_name=models.CharField(max_length=200)
    image=models.ImageField(upload_to='appphoto/')
    link=models.CharField(max_length=200)
    category=models.CharField(max_length=100)
    sub_category=models.CharField(max_length=100)
    total_point=models.IntegerField()


    def __str__(self):
        return "App name : " + self.name + ", Package : " + self.package_name

class Userdata(models.Model):
    username = models.CharField(max_length=200)
    email=models.CharField(max_length=200,default="")
    passowrd=models.CharField(max_length=200)
    isadmin=models.BooleanField(default=False)


class Points(models.Model):
    user=models.ForeignKey(Userdata,on_delete=models.CASCADE)
    app=models.ForeignKey(AppsInfo, on_delete=models.CASCADE)
    state=models.BooleanField(default=False)

class AppImages(models.Model):
    pointid=models.ForeignKey(Points,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/')
