from django.shortcuts import render
from django.shortcuts import HttpResponse,redirect
from django.contrib import messages
from .models import *
# Create your views here.
def login(request):
    if "mymail" not in request.session:
        if request.method=="POST":
            email=request.POST["email"]
            password=request.POST["password"]
            userlogin=Userdata.objects.get(email=email,passowrd=password)
            if userlogin is not None:
                request.session["mymail"]=userlogin.email
                request.session["isadmin"]=userlogin.isadmin
                request.session['userid']=userlogin.pk
                return redirect("/dashboard")
            else:
                messages.info("Email or password is incorrect")
                return render(request, 'login.html')
        return render(request, 'login.html')
    else:
        return redirect('/dashboard')
        #request.session['myname']="deepak"
    #return render(request,'login.html')

def register(request):
    if "mymail" not in request.session:
        if request.method=="POST":
            name= request.POST["name"] if request.POST["name"] else None
            email = request.POST["email"] if request.POST["email"] else None
            password = request.POST["password"] if request.POST["password"] else None
            con_password = request.POST["con_password"] if request.POST["con_password"] else None
            if name is None or email is None or password is None or con_password is None:
                messages.warning(request,"All the Fileds must be filled")
                return render(request, 'register.html')
            elif password != con_password:
                messages.warning(request, "password and confirm password must be same")
                return render(request, 'register.html')
            else:
                newuser=Userdata(username=name,email=email,passowrd=password, isadmin=False)
                newuser.save()
                messages.success(request,"User creaed successfully. Kindly click login to view dashboard")
                request.session['mymail']
                return render(request,'register.html')
        else:
            return render(request, 'register.html')
    else:
        return render(request,'register.html')

def dashboard(request):
    if "userid" in request.session:
        userlogin = Userdata.objects.get(pk=request.session['userid'])
        if userlogin:
            print(userlogin.email)
        return render(request,"dashboard.html",context={"req":request.session,'user':userlogin})
    else:
        return render(request,"dashboard.html")

def logout(request):
    if "mymail" in request.session:
        del request.session['mymail']
        return redirect("/")
    else:
        return redirect("/")


def regdata(request):
    import re
    data = '{"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10},{"id":11},{"id":648},{"id":649},{"id":650},{"id":651},{"id":652},{"id":653}],"errors":[{"code":3,"message":"[PHP Warning #2] count(): Parameter must be an array or an object that implements Countable (153)"}]}'
    lst=[x[1:] for x in re.findall(r':\d{1,5}',data)]
    print(lst)
    return HttpResponse(lst)


def viewApps(request):
    appdata=AppsInfo.objects.all()
    if "mymail" in request.session:
        return render(request,'viewapps.html',{"adddata":appdata})
    else:
        return redirect('/')


def addApp(request):
    if "mymail" in request.session:
        if request.method=="POST" and request.session["isadmin"]==True:
            name = request.POST["appname"]
            package_name = request.POST["package_name"]
            image = request.FILES.get("image") #request.POST["image"]
            link = request.POST["link"]
            category = request.POST["category"]
            sub_category = request.POST["sub_category"]
            total_point = request.POST["points"]
            newapp=AppsInfo(name=name,package_name=package_name,image=image,link=link,category=category,sub_category=sub_category,total_point=total_point)
            newapp.save()
            print(name,package_name,link,category,sub_category,total_point,image)
            return render(request, 'addapp.html')
        else:
            return render(request, 'addapp.html')
    else:
        return redirect('/')
    pass

def deleteApp(request,appid):
    app=AppsInfo.objects.get(pk=appid)
    if app is not None:
        print(app.pk)
        app.delete()
        return redirect('/viewapps')
    else:
        print("No app found")
        return redirect('/viewapps')



def updateApp(request,appid):
    app = AppsInfo.objects.get(pk=appid)
    if request.method=="POST" and app is not None and "mymail" in request.session:
        if request.session["isadmin"] == True:
            app.name = request.POST["appname"]
            app.package_name = request.POST["package_name"]
            if request.FILES.get("image") is not None:
                app.image = request.FILES.get("image")  # request.POST["image"]
            app.link = request.POST["link"]
            app.category = request.POST["category"]
            app.sub_category = request.POST["sub_category"]
            app.total_point = request.POST["points"]
            app.save()
            return redirect('/viewapps')
        else:
            return redirect('/viewapps')
    elif app is not None and "mymail" in request.session:
        if request.session["isadmin"] == True:
            return render(request,"updateapp.html",{"app":app})
        else:
            return redirect('/viewapps')
    else:
        return redirect('/viewapps')


def adduser(request):
    if "mymail" in request.session:
        if request.method == "POST" and request.session["isadmin"] == True:
            name = request.POST["name"] if request.POST["name"] else None
            email = request.POST["email"] if request.POST["email"] else None
            password = request.POST["password"] if request.POST["password"] else None
            con_password = request.POST["con_password"] if request.POST["con_password"] else None
            if name is None or email is None or password is None or con_password is None:
                messages.warning(request, "All the Fileds must be filled")
                return render(request, 'adduser.html')
            elif password != con_password:
                messages.warning(request, "password and confirm password must be same")
                return render(request, 'adduser.html')
            else:
                newuser = Userdata(username=name, email=email, passowrd=password, isadmin=False)
                newuser.save()
                messages.success(request, "User creaed successfully.")
                return render(request, 'adduser.html')
        else:
            return render(request, 'adduser.html')
    else:
        return render(request, 'adduser.html')


def viewusers(request):
    userdata = Userdata.objects.all()
    for user in userdata:
        print(user)
        for point in user.points_set.all():
            print(user,"   ",point.state)

    if "mymail" in request.session:
        return render(request, 'viewusers.html', {"userdata": userdata})
    else:
        return redirect('/')
    pass

def updateuser(request,userid):
    user = AppsInfo.objects.get(pk=userid)
    if "mymail" in request.session:
        if request.method == "POST" and request.session["isadmin"] == True:
            name = request.POST["name"] if request.POST["name"] else None
            email = request.POST["email"] if request.POST["email"] else None
            password = request.POST["password"] if request.POST["password"] else None
            con_password = request.POST["con_password"] if request.POST["con_password"] else None
            if name is None or email is None or password is None or con_password is None:
                messages.warning(request, "All the Fileds must be filled")
                return render(request, 'register.html')
            elif password != con_password:
                messages.warning(request, "password and confirm password must be same")
                return render(request, 'register.html')
            else:
                newuser = Userdata(username=name, email=email, passowrd=password, isadmin=False)
                newuser.save()
                messages.success(request, "User creaed successfully. Kindly click login to view dashboard")
                request.session['mymail']
                return render(request, 'register.html')
        else:
            return render(request, 'register.html')
    else:
        return render(request, 'register.html')


def deleteuser(request,userid):
    user = AppsInfo.objects.get(pk=userid)
    if user is not None:
        print(user.pk)
        user.delete()
        return redirect('/viewapps')
    else:
        print("No app found")
        return redirect('/viewapps')

#user data
def userpoints(request):
    if "userid" in request.session:
        userlogin = Userdata.objects.get(pk=request.session['userid'])
        pointsdata=userlogin.points_set.all()
        print(pointsdata)
        for point in pointsdata:
            print(point.app.total_point)
        if userlogin:
            print(userlogin.email)
        return render(request,"points.html",context={"req":request.session,'user':userlogin,'pointsdata':pointsdata})
    else:
        return render(request,"dashboard.html")

def tasks(request):
    appdata = AppsInfo.objects.all()
    if "mymail" in request.session:
        return render(request, 'viewapps.html', {"adddata": appdata})
    else:
        return redirect('/')
