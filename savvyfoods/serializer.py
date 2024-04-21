from rest_framework.serializers import ModelSerializer
from .models import Junks,Foods,Cart,Restaurant,CartItem

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


class CartItemSerializer(serializers.ModelSerializer):
    item_name = serializers.SerializerMethodField()
    item_image = serializers.SerializerMethodField()
    item_type = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ['id', 'restaurant', 'food', 'junk', 'quantity', 'total_price', 'item_name', 'item_image', 'item_type']
        read_only_fields = ['total_price', 'item_name', 'item_image', 'item_type']

    def get_item_name(self, obj):
        return obj.item_name

    def get_item_image(self, obj):
        return obj.item_image

    def get_item_type(self, obj):
        return obj.item_type

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = ['user', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        cart = Cart.objects.create(**validated_data)
        for item_data in items_data:
            CartItem.objects.create(cart=cart, **item_data)
        return cart

    def update(self, instance, validated_data):
        items_data = validated_data.pop('items')
        instance.items.all().delete()
        for item_data in items_data:
            CartItem.objects.create(cart=instance, **item_data)
        return instance

class CartDeleteSerializer(serializers.Serializer):
    cart_item_id = serializers.IntegerField()
