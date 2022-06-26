from django.shortcuts import render, redirect, get_object_or_404
from .forms import noteform
from .models import note
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
# Create your views here.
def home(request):
    all = note.objects.all()
    return render(request, ('base/home.html'), {
    'all': all
    })
    

def create(request):
    if request.method == "POST":
        title = request.POST['question']
        des = request.POST['answer']
        all = note(title=title, description=des)
        all.save()
        return redirect('home')
    else:
        pass
    return render(request, ('base/create.html'), {})
    
def delete(request, pk):
    item = note.objects.get(id = pk)
    item.delete()
    return redirect('home')
    

def update(request, pk):    
    if request.method == "POST":
        obj = note.objects.get(id = pk)
        form = noteform(request.POST or None, instance = obj)
        if form.is_valid():
            form.save() 
            return redirect('home')
    else:
        form = noteform()
    return render(request, "base/upda.html", {
    'form': form
    })
