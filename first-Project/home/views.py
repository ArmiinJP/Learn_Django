from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.models import Person, Animal
from django.contrib import messages
from home.forms import CreateAnimalForm, UpdateAnimalForm
# Create your views here.

def home(request):
    all = Animal.objects.all()
    return render(request, 'home.html', {'test': all})

def read(request, animal_id):
    data = Animal.objects.get(id=animal_id)
    return render(request, 'detail.html', {'data': data})

def delete(request, animal_id):
    Animal.objects.get(id=animal_id).delete()
    messages.success(request, "deleted successfully", "success")
    return redirect('home')

def create(request):
    #send request from form by user
    if request.method == "POST":
        form = CreateAnimalForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Animal.objects.create(title=cd['title'], body=cd['body'], created=cd['created'])
            messages.success(request, 'successfully', "success")
            return redirect('home')
    else:
        form = CreateAnimalForm()
    
    return render(request, 'create.html', {'form' :form})

def update(request, animal_id):
    animal = Animal.objects.get(id=animal_id)
    if request.method == "POST":
        form = UpdateAnimalForm(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            messages.success(request, "successfully", "success")
            
        return redirect('details',animal_id )
    else:
        form = UpdateAnimalForm(instance=animal)
    return render(request, 'update.html', {'form':form})