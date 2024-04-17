from rest_framework.serializers import ModelSerializer
from .models import Junks,Foods,Orders,Cart,Restaurant

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



class OrderSerializer(ModelSerializer):

    class Meta:
        model=Orders
        fields="__all__"
        


class CartSerializer(ModelSerializer):

    class Meta:
        model=Cart
        fields="__all__"




class CartDeleteSerializer(serializers.Serializer):
    cart_item_id = serializers.IntegerField()
