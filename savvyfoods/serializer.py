from rest_framework.serializers import ModelSerializer
from .models import Junks,Foods,Orders,Cart


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


from rest_framework import serializers

class CartDeleteSerializer(serializers.Serializer):
    cart_item_id = serializers.IntegerField()
