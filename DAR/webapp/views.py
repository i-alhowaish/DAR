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

from django.db.models import Q
from django.db.models import F, ExpressionWrapper, DecimalField

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
from datetime import date

from django.db.models import Count, Q
from django.shortcuts import get_object_or_404, render
from .models import Profile

from django.shortcuts import render, get_object_or_404
from .models import Profile, Favorite

from django.shortcuts import redirect, get_object_or_404
from .models import Profile, Property, Favorite


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
            print('form is valid')
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
            
            return redirect('property_information',new_property.pid)  # Redirect to a new URL after successful creation
    else:
        property_form = PropertyForm()
        images_form = PropertyImagesForm()  # This form might not be directly used in the template but initialized here if needed
        image360_form = PropertyImages360Form()
        return render(request, 'webapp/add_property.html', {'property_form': property_form, 'images_form': images_form, 'images360_form':image360_form })

     


@login_required(login_url='login')
def update_property(request, property_id):
    property_instance = get_object_or_404(Property, pk=property_id)
    if not property_instance.uid == request.user.profile:
        # If it belongs to the user, delete it
        return redirect('')


    
    
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
            
            return redirect('property_information',property_id)  # Redirect to the property detail page
    else:
        property_form = updatePropertyForm(instance=property_instance)
        # Loading existing images is not directly handled here, assuming it's managed through the template or another mechanism
    existing_images = PropertyImages.objects.filter(property=property_instance)
    existing_images360 = PropertyImages360.objects.filter(property360=property_instance)

    context = {
        'property_form': property_form,
        'property_id': property_id,
        'existing_images':existing_images,
        'existing_images360':existing_images360,
        'propertyid':property_id

        # Context for existing images can be added if needed for display or management
    }
    
    return render(request, 'webapp/update_property.html', context)


@login_required(login_url='login')
def my_properties(request):
    profile = Profile.objects.get(user=request.user)
    properties = profile.properties.all()
    return render(request, 'webapp/my_properties.html',{"properties":properties,"profile":profile})







@login_required(login_url='login')
def settings(request):
   
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
            messages.success(request, 'تم تحديث معلوماتك الشخصية بنجاح')
        else:
             messages.error(request,"هناك خطأ باسم المستخدم")

        if password_change_attempted:
            password_form = PasswordChangeForm(user=request.user, data=request.POST)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'تم تحديث الرقم السري بنجاح')
            else:
                messages.error(request, 'كلمة المرور خاطئة، يجب ان تكون اكثر من ٨ خانات و مكونة من احرف وارقام وغير سهلة التوقع')

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




        
def property_information(request, pid):
    property_instance = get_object_or_404(Property, pid=pid)
    profile = get_object_or_404(Profile, id=property_instance.uid.id)
    if request.method == 'POST':
        description= request.POST.get('name')
        r =  Report.objects.create(description=description,date=date.today(),uid=profile,property=property_instance)
        r.save()


        
         

    images = property_instance.images.all()
    images360 = property_instance.images360.all()
    try:
        area = float(property_instance.length) * float(property_instance.width)
    except (ValueError, TypeError):
        area = "Invalid input"  
    ph = profile.phone_number[1:]
    return render(request, 'webapp/property_information.html', { 'ph':ph,'property': property_instance, 'p': profile, 'images': images ,'images360': images360, 'area': area})

@login_required(login_url='login')
def add_to_favorite(request, pid):
    u=Profile.objects.get(user=request.user)
    p=get_object_or_404(Property, pid=pid)
    Favorite.objects.get_or_create(uid=u,property=p)
    # Favorite.objects.create(uid=u,property=p)
    return redirect('property_information',pid)



def search(request):
    properties=Property.objects.all()
    # Pass request.GET directly to the filter_properties function
    if request.method == 'POST':
        print('hello')
        print(request.POST)
        print()
        r = cleandic(request.POST)
        print(r)
        properties = filter_properties(r)

    # Pass filtered properties to the template
    context = {
        'properties': properties
    }
    return render(request, 'webapp/search.html', context)




def filter_properties(di):
    queryset = Property.objects.all()

    # Filter properties based on criteria
    for key, value in di.items():
        if value:
            if key == 'min_price':
                x=value.replace(',','')
                print(x)
                queryset = queryset.filter(price__gte=x)
            elif key == 'max_price':
                x=value.replace(',','')
                queryset = queryset.filter(price__lte=x)
            elif key == 'region':
                queryset = queryset.filter(region=value)
            elif key == 'city':
                print(value)
                queryset = queryset.filter(city=value)
            elif key == 'neighborhood':
                queryset = queryset.filter(neighborhood=value)
            elif key == 'type':
                print(value)
                queryset = queryset.filter(type=value)
            elif key == 'min_size':
                x=value.replace(',','')
                queryset = queryset.annotate(size=F('length') * F('width'))
                queryset = queryset.filter(size__gte=x)
                
            elif key == 'max_size':
                x=value.replace(',','')
                queryset = queryset.annotate(size=F('length') * F('width'))
                queryset = queryset.filter(size__lte=x)
            elif key == 'length':
                x=value.replace(',','')
                queryset = queryset.filter(length=x)
            elif key == 'width':
                x=value.replace(',','')
                queryset = queryset.filter(width=x)
            elif key == 'sell_or_rent':
                queryset = queryset.filter(sell_or_rent=value)
            elif key == 'min_rooms':
                
                if value == '7':
                    print(value)
                    queryset = queryset.filter(number_of_rooms__gte=value)
                else :
                     queryset = queryset.filter(number_of_rooms = value)

            elif key == 'min_bathrooms':
                if value == '7':
                     queryset = queryset.filter(number_of_bathrooms__gte=value)
                else :
                     queryset = queryset.filter(number_of_bathrooms = value)
               

    return queryset

def cleandic(di):
    new={}
    for li in di:
        if di[li] != '':
            new[li]=di[li]
    return new

# Ibrahim: Just for testing you can change abo abo omha 
# def profile(request):
#      return render(request, 'webapp/profile.html')      
def profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)
    properties=Property.objects.filter(uid=profile)
    rent_count = Property.objects.filter(uid=profile,sell_or_rent= "rent").count()
    sell_count = Property.objects.filter(uid=profile,sell_or_rent= "sell").count()
    ph = profile.phone_number[1:]
    return render(request, 'webapp/profile.html', {'ph':ph, 'Profile': profile, 'properties': properties,'rent_count': rent_count,'sell_count': sell_count,})
# Ibrahim: Just for testing you can change abo abo omha 
# def favorate(request):
#      return render(request, 'webapp/favorate.html')  
 
@login_required(login_url='login')
def favorites(request):
    profile = Profile.objects.get(user=request.user)
    favorite_properties = profile.favorites.all()
    
    return render(request, 'webapp/favorate.html', {'favorites': favorite_properties, 'profile': profile})

# Ibrahim: Just for testing you can change abo abo omha 
def dashboard(request):
     return render(request, 'webapp/dashboard.html')   

@login_required(login_url='login')
def remove_from_favorite(request, pid):
    profile = Profile.objects.get(user=request.user)
    property = get_object_or_404(Property, pid=pid)
    favorite = Favorite.objects.filter(uid=profile, property=property)
    if favorite.exists():
        favorite.delete()
    # return redirect(favorites, uid )
    return redirect(request.META.get('HTTP_REFERER', 'fallback_url'))

@login_required(login_url='login')
def delete_property(request,pid):
    #property_instance = get_object_or_404(Property, pk=property_id)
    property_instance = get_object_or_404(Property, pid=pid)
    
    # Check if the property belongs to the current user
    if property_instance.uid == request.user.profile:
        # If it belongs to the user, delete it
        property_instance.delete()
    
    return redirect('my_properties')

