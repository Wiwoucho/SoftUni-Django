from django.shortcuts import render, redirect
from .forms import ProfileBaseFrom, ProfileEditForm
from .models import Profile
from ..fruit_id.models import Fruits


def profile_create(request):
    if request.method == 'GET':
        form = ProfileBaseFrom()
    else:
        form = ProfileBaseFrom(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
    }

    return render(request, 'create-profile.html', context)


def profile_details(request):
    fruits = Fruits.objects.count()
    profile = Profile.objects.get()
    context = {
        'profile': profile,
        'fruits': fruits
    }
    return render(request, 'details-profile.html', context)


def profile_edit(request):
    profile = Profile.objects.get()
    if request.method == 'GET':
        form = ProfileEditForm(instance = profile)
    else:
        form = ProfileEditForm(request.POST or None, instance = profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')

    context = {
        'form': form
    }

    return render(request, 'edit-profile.html', context)



def profile_delete(request):
    fruits = Fruits.objects.all()
    profile = Profile.objects.get()
    if request.method == "POST":
        fruits.delete()
        profile.delete()
        return redirect('index')


    return render(request, 'delete-profile.html')
