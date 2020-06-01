from django.shortcuts import render
from django.http import HttpResponse
from . import models
import sqlite3




# Create your views here.
def Index(request):
    return render(request,'index.html')



def register(request):



    return render(request,'register.html')

def sorry(request):
    return render(request,'sorry.html')

def login(request):
    return render(request,'login.html')

def login_done(request):
    regobj = models.Register()


    lemail=request.POST.get('user_email')
    lpass=request.POST.get('user_pswd')
    # all=[name,mail,phone,psw,pswr]

    # for registration
    mail=regobj.mail
    psw=regobj.psw

    if lemail==lpass:
        return render(request, 'login_done.html')
    else:
        return render(request, 'sorry.html')






def reg_done(request):
    regobj=models.Register()

    name=request.POST.get('user_name')
    mail = request.POST.get('user_email')
    phone = request.POST.get('user_phone')
    psw = request.POST.get('user_password')
    pswr = request.POST.get('urepeat_password')
    # all=[name,mail,phone,psw,pswr]

    # for registration
    regobj.name=name
    regobj.mail=mail
    regobj.phone=phone
    regobj.psw=psw
    regobj.pswr=pswr
    regobj.save()


    return render(request,'reg_done.html')
