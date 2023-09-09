from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from . models import *




def signup(request):
    if request.method== 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password") 
        password2 = request.POST.get("conformpassword")
        
        if password1!=password2 :
            return redirect("signup")
        else :
            my_user=User.objects.create_user(username,email,password1)
            my_user.save()
            return redirect ("signin")

    return render(request,"signup.html")

def signin(request):
    if request.method=="POST":
        username=request.POST.get("username")
        pass1=request.POST.get("password")

        user=authenticate(request,username=username,password=pass1)
        
        if user is not None:
            login(request,user)
            return redirect("home")
        else :
            return redirect("signup")
       
    return render(request,"signin.html")

def home(request):
    return render (request,'home.html')

def newmeeting(request):
    return render(request,'newmeeting.html')


def joinmeeting(request):
    if request.method == 'POST':
        roomID = request.POST['roomID']
        return redirect("/newmeeting?roomID=" + roomID)
    return render(request, 'joinmeeting.html')


def signout(request):
    logout(request)
    return('signin')    