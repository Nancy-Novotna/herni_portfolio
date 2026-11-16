from django.shortcuts import render

from main.models import Games



# Create your views here.


def index(request):
    return render(request, "main/index.php")


def hry(request):
    games = Games.objects.all()
    return render(request, "main/games.php", {
        'games': games
    })
