from django.shortcuts import render, redirect

from WebBasicsExam.user_profile.models import Profile
from WebBasicsExam.fruit_id.models import Fruits
from ..fruit_id.forms import FruitBaseForm

def dashboard(request):
    fruits = Fruits.objects.all()
    context = {
        'fruits': fruits
    }
    return render(request, 'dashboard.html', context)


def create(request):
    if request.method == 'GET':
        form = FruitBaseForm()
    else:
        form = FruitBaseForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {'form': form}

    return render(request, 'create-fruit.html', context)

def index(request):
    return render(request, 'index.html')
