# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Availability(models.Model):
    id_avail = models.IntegerField(primary_key=True)
    platform = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'availability'


class Developer(models.Model):
    id_dev = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    residence = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'developer'


class FilterAvail(models.Model):
    id_game = models.ForeignKey(
        'Games', models.DO_NOTHING, db_column='id_game')
    id_avail = models.ForeignKey(
        Availability, models.DO_NOTHING, db_column='id_avail')

    class Meta:
        managed = False
        db_table = 'filter_avail'


class FilterDev(models.Model):
    id_game = models.ForeignKey(
        'Games', models.DO_NOTHING, db_column='id_game')
    id_dev = models.ForeignKey(
        Developer, models.DO_NOTHING, db_column='id_dev')

    class Meta:
        managed = False
        db_table = 'filter_dev'



class FilterGenre(models.Model):
    id_game = models.ForeignKey(
        'Games', models.DO_NOTHING, db_column='id_game')
    id_genre = models.ForeignKey(
        'Genre', models.DO_NOTHING, db_column='id_genre')

    class Meta:
        managed = False
        db_table = 'filter_genre'


class FilterPub(models.Model):
    id_game = models.ForeignKey(
        'Games', models.DO_NOTHING, db_column='id_game')
    id_pub = models.ForeignKey(
        'Publisher', models.DO_NOTHING, db_column='id_pub')

    class Meta:
        managed = False
        db_table = 'filter_pub'


class Games(models.Model):
    id_game = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    release_date = models.DateField()
    price = models.FloatField()
    consultation = models.IntegerField()
    platinum = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'games'


class Genre(models.Model):
    id_genre = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'genre'


class Publisher(models.Model):
    id_pub = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    residence = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'publisher'
