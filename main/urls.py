from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("lidi/", views.jmena, name="people"),
    # path("<slug:slug>/", views.videogame, name="videogame"),
]