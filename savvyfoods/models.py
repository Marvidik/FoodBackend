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
    opening_hour=models.TimeField(default=datetime.now())
    closing_hour=models.TimeField(default=datetime.now())


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



class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField('CartItem')

    def __str__(self):

        return self.user.username

class CartItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    food = models.ForeignKey(Foods, on_delete=models.CASCADE, null=True, blank=True)
    junk = models.ForeignKey(Junks, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.IntegerField()

    @property
    def item_name(self):
        return self.food.name if self.food else self.junk.name

    @property
    def item_image(self):
        return self.food.image.url if self.food else self.junk.image.url

    @property
    def item_type(self):
        return 'Food' if self.food else 'Junk'

    def save(self, *args, **kwargs):
        if not self.pk:  # New instance
            if self.food:
                self.total_price = self.quantity * self.food.price
            elif self.junk:
                self.total_price = self.quantity * self.junk.price
        super().save(*args, **kwargs)