from django.shortcuts import render
from .models import Names


# Create your views here.


def index(request):
    return render(request, "main/index.php")


def jmena(request):
    names = Names.objects.using('xampp').all()
    return render(request, "main/index.php", {
        'names': names
    })
