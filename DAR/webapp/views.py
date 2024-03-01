from django.shortcuts import render,redirect
from .forms import LoginForm,RegisterForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *
import json 

from django.contrib import messages

# Create your views here.
from django.http import JsonResponse
import os


def jdata(request):
    file_path = 'locationsJSON/location1.json'
    with open(file_path, 'r', encoding="utf-8") as json_file:
        data = json.load(json_file)#json_file.read()
    return JsonResponse(data, safe=False)

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

@login_required(login_url='login')  # Use the name of your login URL
def add_property(request):
    if request.method == 'POST':
        property_form = PropertyForm(request.POST)
        if property_form.is_valid():
            new_property = property_form.save(commit=False)
            new_property.uid = request.user  # Assign the logged in user
            new_property.save()
            
            images_files = request.FILES.getlist('images')
            for image_file in images_files:
                PropertyImages.objects.create(property=new_property, image=image_file)
            
            #return redirect('some_view')  # Redirect to a new URL after successful creation
            
            
            images360_files = request.FILES.getlist('images360')
            for image_file in images360_files:
                PropertyImages360.objects.create(property360=new_property, image360=image_file)
            
            return redirect('some_view')  # Redirect to a new URL after successful creation
    else:
        property_form = PropertyForm()
        images_form = PropertyImagesForm()  # This form might not be directly used in the template but initialized here if needed
        image360_form = PropertyImages360Form()
        
    
    return render(request, 'webapp/add_property.html', {'property_form': property_form, 'images_form': images_form, 'images360_form':image360_form })

     