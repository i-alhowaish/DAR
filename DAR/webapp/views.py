from django.shortcuts import render
from .forms import LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from django.contrib import messages

# Create your views here.


def testing(request):
    return render(request, 'webapp/index.html')


def login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            print(username, password)
            
    context = {'form':form}
    return render(request, 'webapp/login.html', context)


def register(request):
    return render(request, 'webapp/register.html')