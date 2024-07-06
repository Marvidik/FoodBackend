from rest_framework.serializers import ModelSerializer
from .models import Junks,Foods,Restaurant,Cart,Order,Advert,Notification

from rest_framework import serializers



class RestaurantSerializer(ModelSerializer):

    class Meta:
        model=Restaurant
        fields="__all__"


class JunkSerializer(ModelSerializer):

    class Meta:
        model=Junks
        fields="__all__"



class FoodsSerializer(ModelSerializer):


    class Meta:
        model=Foods
        fields="__all__"



class CartSerializer(ModelSerializer):

    class Meta:
        model=Cart
        fields="__all__"



class OrderSerializer(ModelSerializer):

    class Meta:
        model=Order
        fields="__all__"

    def get_food_count(self, obj):
        return Order.objects.filter(user=obj.user, delivered=False).count()


class AdvertSerializer(ModelSerializer):

    class Meta:
        model=Advert
        fields="__all__"


class NotSerializer(ModelSerializer):

    class Meta:
        model=Notification
        fields="__all__"