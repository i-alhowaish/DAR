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

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Property, PropertyImages, PropertyImages360
from .forms import updatePropertyForm, PropertyImagesForm, PropertyImages360Form


from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserSettingsForm

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserSettingsForm

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
        print('form is post')
        property_form = PropertyForm(request.POST)
        if property_form.is_valid():
            print('form is post')
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

     


@login_required(login_url='login')
def update_property(request, property_id):
    property_instance = get_object_or_404(Property, pk=property_id)
    
    if request.method == 'POST':
        property_form = updatePropertyForm(request.POST, request.FILES, instance=property_instance)
        
        if property_form.is_valid():
            updated_property = property_form.save()
            
            # Handling standard images update or addition
            # PropertyImages.objects.filter(property=updated_property).delete()
            images_to_delete = request.POST.getlist('delete_images')
            PropertyImages.objects.filter(id__in=images_to_delete).delete()

            images_files = request.FILES.getlist('images')
            for image_file in images_files:
                PropertyImages.objects.create(property=updated_property, image=image_file)
            
            # Handling 360 images update or addition
            images_to_delete360 = request.POST.getlist('delete_images360')
            PropertyImages360.objects.filter(id__in=images_to_delete360).delete()
            images360_files = request.FILES.getlist('images360')
            for image_file in images360_files:
                PropertyImages360.objects.create(property360=updated_property, image360=image_file)
            
            return redirect('property_detail', pk=updated_property.pk)  # Redirect to the property detail page
    else:
        property_form = updatePropertyForm(instance=property_instance)
        # Loading existing images is not directly handled here, assuming it's managed through the template or another mechanism
    existing_images = PropertyImages.objects.filter(property=property_instance)
    existing_images360 = PropertyImages360.objects.filter(property360=property_instance)

    context = {
        'property_form': property_form,
        'property_id': property_id,
        'existing_images':existing_images,
        'existing_images360':existing_images360

        # Context for existing images can be added if needed for display or management
    }
    
    return render(request, 'webapp/update_property.html', context)


# @login_required(login_url='login')  # Use the name of your login URL
# def update_property(request, property_id):
#     property_instance = get_object_or_404(Property, pk=property_id)
    
#     if request.method == 'POST':
#         property_form = PropertyForm(request.POST, instance=property_instance)
#         if property_form.is_valid():
#             updated_property = property_form.save()
            
#             images_files = request.FILES.getlist('images')
#             PropertyImages.objects.filter(property=updated_property).delete()  # Optionally delete existing images to replace them
#             for image_file in images_files:
#                 PropertyImages.objects.create(property=updated_property, image=image_file)
            
#             images360_files = request.FILES.getlist('images360')
#             PropertyImages360.objects.filter(property360=updated_property).delete()  # Optionally delete existing 360 images to replace them
#             for image_file in images360_files:
#                 PropertyImages360.objects.create(property360=updated_property, image360=image_file)
            
#             return redirect('some_view')  # Redirect to a new URL after successful update
#     else:
#         property_form = PropertyForm(instance=property_instance)
#         # images_form and images360_form might not be directly used if you're handling file inputs separately
#         images_form = PropertyImagesForm()  # Initialize if needed for template
#         images360_form = PropertyImages360Form()  # Initialize if needed for template

#     # Fetch existing images if you want to display them in the template
#     existing_images = PropertyImages.objects.filter(property=property_instance)
#     existing_images360 = PropertyImages360.objects.filter(property360=property_instance)

#     context = {
#         'property_form': property_form,
#         'images_form': images_form,
#         'images360_form': images360_form,
#         'existing_images': existing_images,
#         'existing_images360': existing_images360,
#         'property_id': property_id  # Pass property ID to template for use in form action URL
#     }
    
#     return render(request, 'webapp/update_property.html', context)   




@login_required(login_url='login')
def settings(request):
    if request.method == 'POST':
        form = UserSettingsForm(request.POST, instance=request.user, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your settings have been updated.')
            return redirect('settings_url_name')  # Adjust as needed
    else:
        form = UserSettingsForm(instance=request.user, user=request.user)
    return render(request, 'path/to/your_template.html', {'form': form})