from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response


from .models import Junks,Foods,Restaurant,Cart,Order,Advert
from .serializer import JunkSerializer,FoodsSerializer,RestaurantSerializer,CartSerializer,OrderSerializer,AdvertSerializer
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


@api_view(['GET'])
def view_cart(request,id):

    data=Cart.objects.filter(user=id)
    serializer=CartSerializer(instance=data, many=True)

    return Response({'Cart': serializer.data}, status=status.HTTP_200_OK)


@api_view(["POST"])
def add_to_cart(request):

    serializer= CartSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({'Cart':"Done"}, status=status.HTTP_200_OK)
    else:
        return Response({'Cart':"error"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE","GET"])
def remove_from_cart(request, id):
    try:
        cart_item = Cart.objects.get(pk=id)
        cart_item.delete()
        return Response({'message': 'Item removed from cart successfully.'}, status=status.HTTP_200_OK)
    except Cart.DoesNotExist:
        return Response({'error': 'Cart item not found.'}, status=status.HTTP_404_NOT_FOUND)
    

@api_view(['GET'])
def view_orders(request, id):
    orders = Order.objects.filter(user=id)
    order_data = []
    
    for order in orders:
        order_details = OrderSerializer(order).data
        food_details = None
        junk_details = None
        
        # Fetch food details if available
        if order.real_food:
            food_details = {
                'name': order.real_food.name,
                'image': order.real_food.image.url,
                'rating': order.real_food.rating,
                'deliveryfee': order.real_food.deliveryfee,
                'category': order.real_food.category,
                'availability': order.real_food.availability,
                'price': order.real_food.price
            }
        
        # Fetch junk details if available
        if order.real_junk:
            junk_details = {
                'name': order.real_junk.name,
                'image': order.real_junk.image.url,
                'rating': order.real_junk.rating,
                'deliveryfee': order.real_junk.deliveryfee,
                'category': order.real_junk.category,
                'availability': order.real_junk.availability,
                'price': order.real_junk.price
            }
        
        order_details['food_details'] = food_details
        order_details['junk_details'] = junk_details
        order_data.append(order_details)

    return Response({'Orders': order_data}, status=status.HTTP_200_OK)

@api_view(["POST"])
def add_to_order(request):

    serializer= OrderSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({'Orders':"Orders Successfuly Added"}, status=status.HTTP_200_OK)
    else:
        return Response({'Order':"error"}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["PATCH"])
def received(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response({"message": "Order not found"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "PATCH":
        serializer = OrderSerializer(order, data={'delivered': True}, partial=True)
        if serializer.is_valid():
            serializer.save()  # Commit changes to the database
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



@api_view(['GET'])
def advert(request):
    data=Advert.objects.all()

    serializer=AdvertSerializer(instance=data,many=True)

    return Response({'ads': serializer.data}, status=status.HTTP_200_OK)