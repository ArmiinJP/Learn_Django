from django.shortcuts import render, redirect
from django.http import HttpResponse
from accounts.forms import RegisterUserForm, LoginUserForm
from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

# Create your views here.

def user_register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['username'], cd['email'], cd['password'])
            user.last_name = cd['last_name']
            user.save()
            messages.success(request, 'successfully', "success")
            return redirect('home')            
    else:
        form = RegisterUserForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == "POST":
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username = cd['username'], password = cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'successfully', "success")
                return redirect('home')              
            else:
                messages.error(request, 'Error Login', "danger")                
    else:
        form = LoginUserForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.success(request, "logout successfully", "success")
    return redirect('home')