from django.shortcuts import render,redirect
from .forms import LoginForm,RegisterForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
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

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.http import JsonResponse
import os

from django.shortcuts import render, get_object_or_404
from .models import Property


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
            u=form.save()
            phone_number = request.POST.get('phone_number', '')
            p = Profile(phone_number=phone_number,user=u)
            p.save()
            # u.profile.phone_number = phone_number
            # u.profile.save()
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
            u=Profile.objects.get(user=request.user)
            new_property.uid = u  # Assign the logged in user
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




# @login_required(login_url='login')
# def settings(request):
#     if request.method == 'POST':
#         form = UserSettingsForm(request.POST, instance=request.user, user=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Your settings have been updated.')
#             return redirect('settings_url_name')  # Adjust as needed
#     else:
#         form = UserSettingsForm(instance=request.user, user=request.user)
#     return render(request, 'webapp/settings.html', {'form': form})

# @login_required(login_url='login')
# def settings(request):
    
#     return render(request, 'webapp/settings.html')



@login_required(login_url='login')
def settings(request):
    # if request.method == 'POST':
    #     form = UserSettingsForm(request.POST, instance=request.user)
    #     if form.is_valid():
    #         user = form.save()
    #         # Example: Save "color of account" to the session
    #         # request.session['color_of_account'] = form.cleaned_data['color_of_account']
    #         messages.success(request, 'Your settings have been updated.')
    #         return redirect('settings')  # Redirect to a confirmation or the settings page itself
    # else:
    #     form = UserSettingsForm(instance=request.user)
    #     # Optional: Initialize form with session data
    #     #if 'color_of_account' in request.session:
    #         #form.fields['color_of_account'].initial = request.session['color_of_account']
    
    # return render(request, 'webapp/settings.html', {'form': form})
    user_form = UserSettingsForm(request.POST or None, instance=request.user)
    password_change_attempted = 'old_password' in request.POST and request.POST['old_password']

    if request.method == 'POST':
        if user_form.is_valid():
            user_form.save()
            profile, created = Profile.objects.get_or_create(user=request.user)
            profile.phone_number = user_form.cleaned_data['phone_number']
            profile.color = user_form.cleaned_data['color_of_account']
            image_file = request.FILES.get('image')
            if image_file:  # Check if file uploaded
                profile.userimage = image_file
            else :
                want_to_delete=request.POST.getlist('deletion')
                if want_to_delete:
                    profile.userimage = image_file

            profile.save()
            messages.success(request, 'Your settings have been updated.')

        if password_change_attempted:
            password_form = PasswordChangeForm(user=request.user, data=request.POST)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Your password was successfully updated.')
            else:
                messages.error(request, 'There was an error changing your password.')

        return redirect('settings')
       
    else:
        user_form = UserSettingsForm(instance=request.user)
        password_form = PasswordChangeForm(user=request.user)
        p=Profile.objects.get(user=request.user)
    if not p.userimage.name :
        img='https://t4.ftcdn.net/jpg/02/15/84/43/360_F_215844325_ttX9YiIIyeaR7Ne6EaLLjMAmy4GvPC69.jpg'
    else:
        img = p.userimage.url
    context = {
        'user_form': user_form,
        'password_form': password_form,
        'image':img
    }
    return render(request, 'webapp/settings.html', context)


# def property_information(request):
#     return render(request, 'webapp/property_information.html')



# def property_information(request, pid):
#     property = get_object_or_404(Property, pid=pid)
#     p =  get_object_or_404(Profile, user_id=property.uid)
#     u =  get_object_or_404(User, id=p.id)
#     return render(request, 'webapp/property_information.html', {'property': property , 'p':p })

        
def property_information(request, pid):
    property_instance = get_object_or_404(Property, pid=pid)
    profile = get_object_or_404(Profile, id=property_instance.uid.id)
    images = property_instance.images.all()
    images360 = property_instance.images360.all()
    try:
        area = float(property_instance.length) * float(property_instance.width)
    except (ValueError, TypeError):
        area = "Invalid input"  
    return render(request, 'webapp/property_information.html', {'property': property_instance, 'p': profile, 'images': images ,'images360': images360, 'area': area})

def add_to_favorite(request, pid):
    u=Profile.objects.get(user=request.user)
    p=get_object_or_404(Property, pid=pid)
    Favorite.objects.create(uid=u,property=p)

# def report(request, pid):
#     u=Profile.objects.get(user=request.user)
#     p=get_object_or_404(Property, pid=pid)
#     Favorite.objects.create()



