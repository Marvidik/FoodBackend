from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response


from .models import Junks,Foods,Cart,Restaurant,CartItem
from .serializer import JunkSerializer,FoodsSerializer,CartSerializer,CartDeleteSerializer,RestaurantSerializer,CartItemSerializer
# Create your views here.


@api_view(['GET'])
def restaurants(request):
    data=Restaurant.objects.all()

    serializer=RestaurantSerializer(instance=data,many=True)

    return Response({'restaurants': serializer.data}, status=status.HTTP_200_OK)

@api_view(["GET"])
def restaurant_food(request,id):

    data=Foods.objects.filter(restaurant=id)
    serializer=FoodsSerializer(instance=data, many=True)

    return Response({'Foods': serializer.data}, status=status.HTTP_200_OK)


@api_view(["GET"])
def restaurant_junk(request,id):

    data=Junks.objects.filter(restaurant=id)
    serializer=JunkSerializer(instance=data, many=True)

    return Response({'Junks': serializer.data}, status=status.HTTP_200_OK)


@api_view(['POST'])
def add_to_cart(request):
    user = User.objects.get(id=2)

    data = request.data
    cart_items = data.get('cart_items', [])

    try:
        cart = Cart.objects.get(user=user)
    except Cart.DoesNotExist:
        cart = Cart.objects.create(user=user)

    for item_data in cart_items:
        serializer = CartItemSerializer(data=item_data)
        if serializer.is_valid():
            serializer.save(cart=cart)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({"message": "Items added to cart successfully"}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def remove_from_cart(request):
    user = request.user
    if not user.is_authenticated:
        return Response({"error": "User not authenticated"}, status=status.HTTP_401_UNAUTHORIZED)

    data = request.data
    item_ids = data.get('item_ids', [])

    try:
        cart = Cart.objects.get(user=user)
    except Cart.DoesNotExist:
        return Response({"error": "Cart not found for the user"}, status=status.HTTP_404_NOT_FOUND)

    cart_items = CartItem.objects.filter(id__in=item_ids)
    cart_items.delete()

    return Response({"message": "Items removed from cart successfully"}, status=status.HTTP_200_OK)

@api_view(['GET'])
def view_cart(request):
    user = request.user
    if not user.is_authenticated:
        return Response({"error": "User not authenticated"}, status=status.HTTP_401_UNAUTHORIZED)

    try:
        cart = Cart.objects.get(user=user)
    except Cart.DoesNotExist:
        return Response({"error": "Cart not found for the user"}, status=status.HTTP_404_NOT_FOUND)

    cart_items = cart.items.all()
    serializer = CartItemSerializer(cart_items, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)