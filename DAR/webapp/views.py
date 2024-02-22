from django.shortcuts import render,redirect
from .forms import LoginForm,RegisterForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *

from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'webapp/index.html')


def login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            u = authenticate(request, username=username, password=password)
            if u is not None:
                auth.login(request, u)
                return redirect("")
        messages.error(request, 'اسم المستخدم غير صحيح او كلمة المرور خاطئة')

        

            
                #return HttpResponseRedirect(reverse("index"))
            # else in this place
        #else in this place

            
            
    context = {'form':form}
    return render(request, 'webapp/login.html', context)


def register(request):
    form = RegisterForm()

    if request.method == "POST":
        print('post is okay')

        form = RegisterForm(request.POST)

        if form.is_valid():
            print('form is valid')
            form.save()
            return redirect("login")
        #print('form is invalid')
        k=form.errors.as_data()
        print(form.errors.as_data())
        for i in k.keys():
            print(i)
            if i == 'username':
                messages.error(request, 'اسم المستخدم مستخدم من قبل او خاطئ')
            if i == 'password1'or i=='password2':
                messages.error(request, 'كلمة المرور خاطئة، يجب ان تكون اكثر من ٨ خانات و مكونة من احرف وارقام وغير سهلة التوقع')
            if i=='email':
                messages.error(request, 'بريد الكتروني خاطئ')
            # phone number needs to be cheked



       # messages.success(request, form.errors.as_data())
    # form=RegisterForm()
    # if request.method == "POST":
    #     form = RegisterForm(request, data=request.POST)
    #     if form.is_valid():
    #         form.save()
    #         username = request.POST.get('username')
    #         password = request.POST.get('password')
    #         fname = request.POST.get('fname')
    #         lname = request.POST.get('lname')
    #         email = request.POST.get('email')
    #         phone_number = request.POST.get('phone_number')
    #         if not User.objects.filter(username=username).exists():
    #             u = User.objects.create_user(username=username,password=password,first_name=fname , last_name=lname,email=email)
    #             nu = user(us=u,phone_number=phone_number)
    #             nu.save()
    #             login(request,nu)

            #else in this place
        # else in this place

             

    context = {'form':form}
    return render(request, 'webapp/register.html',context)
def userlogout(request):

    auth.logout(request)

    messages.success(request, "Logout success!")

    return redirect("")