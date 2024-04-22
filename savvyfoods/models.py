from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Referal(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    point=models.IntegerField()


class Restaurant(models.Model):
    name=models.CharField(max_length=100)
    logo=models.ImageField(upload_to="retaurants_logos")
    location=models.CharField(max_length=100,default=None)
    opening_hour=models.TimeField()
    closing_hour=models.TimeField()


    def __str__(self):

        return self.name + " (" + (self.location)+ ")"

class Junks(models.Model):
    restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE,default=None)
    name=models.CharField(max_length=100) 
    junk=models.CharField(max_length=100)
    image=models.ImageField(upload_to="junks")
    price=models.IntegerField()
    rating=models.IntegerField()
    deliveryfee=models.IntegerField()
    category=models.CharField(max_length=20)
    availability=models.CharField(max_length=20)
    price=models.IntegerField()


    def __str__(self):

        return self.name




class Foods(models.Model):
    restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE,default=None)
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to="foods")
    contents=models.CharField(max_length=100)
    rating=models.IntegerField()
    deliveryfee=models.IntegerField()
    category=models.CharField(max_length=20)
    availability=models.TextField()
    price=models.IntegerField()

    def __str__(self):

        return self.name



