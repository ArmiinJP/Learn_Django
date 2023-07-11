from django.shortcuts import render, redirect
from django.contrib import auth, messages
from accounts import forms
from todolist import models, forms

from django.contrib.auth.decorators import login_required

@login_required(login_url='/user/login/')
def menu(request):
    all_todo = models.Todo.objects.all()
    return render(request, 'menu.html', {'todos': all_todo})

@login_required(login_url='/user/login/')
def detail(request, todo_id):
    todo = models.Todo.objects.get(id=todo_id)
    return render(request, 'detail.html', {'todo': todo})

@login_required(login_url='/user/login/')
def create(request):
    if request.method == "POST":
        form = forms.CreateTodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "successfully created todo", "success")
            return redirect('menu')
        else:
            messages.error(request, "unsuccessfully create Form", "danger")
            return redirect('menu')
    else:
        form = forms.CreateTodoForm()
        return render(request, 'create.html', {'create_form': form})

@login_required(login_url='/user/login/')
def update(request, todo_id):
    todo = models.Todo.objects.get(id=todo_id)
    if request.method == "POST":
        form = forms.UpdateTodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, "successfully", "success")
            return redirect('menu')
        else:
            messages.error(request, "Unsuccessfully update todo", "danger")
            return redirect('menu')
    else:
        form = forms.UpdateTodoForm(instance=todo)
        return render(request, 'update.html', {'update_form': form})        

@login_required(login_url='/user/login/')    
def delete(request, todo_id):
    todo = models.Todo.objects.get(id=todo_id).delete()
    messages.success(request, "todo Successfully deleted", 'success')
    return redirect('menu')
