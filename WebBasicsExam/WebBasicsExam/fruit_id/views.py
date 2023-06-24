from django.shortcuts import render, redirect
from .models import Fruits
from .forms import FruitEditForm, FruitDeleteForm


def fruit_details(request, pk):
    fruit = Fruits.objects.filter(pk=pk).get()
    context = {
        'fruit': fruit
    }
    return render(request, 'details-fruit.html', context)

def fruit_edit(request, pk):
    fruit = Fruits.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = FruitEditForm(instance = fruit)
    else:
        form = FruitEditForm(request.POST or None, instance = fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'form': form
    }
    return render(request, 'edit-fruit.html', context)

def fruit_delete(request, pk):
    fruit = Fruits.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = FruitDeleteForm(instance = fruit)
    else:
        form = FruitDeleteForm(request.POST or None, instance = fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form
    }

    return render(request, 'delete-fruit.html', context)