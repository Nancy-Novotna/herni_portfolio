from django.shortcuts import render
from django.db import connection
from main.models import *


# Create your views here.


def index(request):
    return render(request, "main/index.php")


def hry(request):
    games = Games.objects.all()
    devs = Developer.objects.all()

    with connection.cursor() as cursor:
        cursor.execute("""
                    SELECT `games`.`title`, `genre`.`type`
                    FROM `games`, `genre`, `filter_genre`
                    WHERE `filter_genre`.`id_game`=`games`.`id_game` AND `filter_genre`.`id_genre`=`genre`.`id_genre`;
                    """)
        genres = cursor.fetchall()


    return render(request, "main/games.php", {
        'games': games,
        'devs': devs,
        'genres': genres,
    })
