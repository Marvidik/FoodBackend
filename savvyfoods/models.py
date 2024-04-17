from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Restaurant(models.Model):
    name=models.CharField(max_length=100)
    logo=models.ImageField(upload_to="retaurants_logos")
    location=models.CharField(max_length=100,default=None)

class Junks(models.Model):
    junk=models.CharField(max_length=100)
    image=models.ImageField(upload_to="junks")
    price=models.IntegerField()
    rating=models.IntegerField()
    deliveryfee=models.IntegerField()
    deliverytime=models.CharField(max_length=20)
    description=models.TextField()
    price=models.IntegerField()




class Foods(models.Model):
    restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE,default=None)
    image=models.ImageField(upload_to="foods")
    contents=models.CharField(max_length=100)
    rating=models.IntegerField()
    deliveryfee=models.IntegerField()
    deliverytime=models.CharField(max_length=20)
    availability=models.TextField()
    price=models.IntegerField()



class Orders(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.CharField(max_length=100)
    orders=models.TextField(max_length=100)
    paid=models.BooleanField(default=False)
    delivered=models.BooleanField(default=False)
    

    def __str__(self) -> str:
        return self.user.username
    

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    order=models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.user.username