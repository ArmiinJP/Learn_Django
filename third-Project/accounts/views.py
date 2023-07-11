from django.shortcuts import render, redirect
from accounts import forms
from django.contrib import auth, messages

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.


def register_user(request):
    if request.method == 'POST':
        form = forms.RegisterUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['username'], cd['email'], cd['password'])
            user.last_name = cd['last_name']
            user.first_name = cd['first_name']
            user.save()
            messages.success(request, 'user successfully regiseterd', 'success')
            return redirect('login')
        else:
            messages.error(request, "register user unsuccessfully", "danger")
            return redirect('register')
    else: 
        form = forms.RegisterUserForm()
        return render(request, 'register.html', {'form':form})

def login_user(request):
    if request.method == 'POST':
        form = forms.LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = auth.authenticate(username = cd['username'], password = cd['password'])
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'user successfully login', "success")
                return redirect('menu')
            else:
                messages.error(request, "login user unsuccessfully", "danger")
                return redirect('login')

            
    else: 
        form = forms.LoginUserForm()
    return render(request, 'login.html', {'form':form})

@login_required(login_url='/user/login/')    
def logout_user(request):
    auth.logout(request)
    messages.success(request, "logout successfully", "success")
    return redirect('login')

@login_required(login_url='/user/login/')    
def home_user(request):
    return render(request, 'home_user.html')