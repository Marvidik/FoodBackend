from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from authentication.models import Profile

# Create your models here.



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
    image=models.ImageField(upload_to="junks")
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
    rating=models.IntegerField()
    deliveryfee=models.IntegerField()
    category=models.CharField(max_length=20)
    availability=models.TextField()
    price=models.IntegerField()

    def __str__(self):

        return self.name


class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to="foods",null=True)
    rating=models.IntegerField()
    deliveryfee=models.IntegerField()
    category=models.CharField(max_length=20)
    price=models.IntegerField()
    quantity=models.IntegerField(default=1)

    def __str__(self):

        return self.user.username


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    real_food = models.ForeignKey(Foods, on_delete=models.CASCADE, null=True, blank=True)
    real_junk = models.ForeignKey(Junks, on_delete=models.CASCADE, null=True, blank=True)
    delivered = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.user.username


class Advert(models.Model):
    image=models.ImageField(upload_to="adverts",null=True)