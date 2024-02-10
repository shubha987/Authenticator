from django.shortcuts import render,redirect,HttpResponse
from datetime import datetime
from login.models import User
from django.contrib.auth import authenticate,login as auth_login,logout


# Create your views here.

def login(request):
    if request.method=='POST':
        firstname=request.POST.get('fname')
        password2=request.POST.get('password')
        print("Firstname:", firstname)
        print("Password:", password2)
        user_model=authenticate(request,username=firstname,password=password2)
        print("Authenticated User:", user_model)
        if user_model is not None:
            auth_login(request,user_model)
            return redirect('home')
        else:
            return HttpResponse("email or password is incorrect!!!")
    return render(request, 'index.html')

def register(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        repassword=request.POST.get('repassword')
        if password!=repassword:
            return HttpResponse('your password didnt match')
        else:

         my_user=User(
            firstname=fname,
            lastname=lname,
            email=email,
            password=password,
            repassword=repassword,
            date=datetime.today())
         my_user.save()   
         return redirect('login')
    return render(request,'register.html')

def home(request):
    return render(request,'home.html')

def logout(request):
    logout(request)
    return redirect('login')