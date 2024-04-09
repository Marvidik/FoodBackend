from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response


from .models import Junks,Foods,Cart
from .serializer import JunkSerializer,FoodsSerializer,OrderSerializer,CartSerializer,CartDeleteSerializer
# Create your views here.



@api_view(['GET'])
def junks(request):
    data=Junks.objects.all()

    serializer=JunkSerializer(instance=data, many=True)

    return Response({'junks': serializer.data}, status=status.HTTP_200_OK)

@api_view(['GET'])
def foods(request):
    data=Foods.objects.all()

    serializer=FoodsSerializer(instance=data, many=True)

    return Response({'junks': serializer.data}, status=status.HTTP_200_OK)


@api_view(['POST'])
def order(request):
    data=request.data 

    serializer=OrderSerializer(data=data)

    if serializer.is_valid():
        serializer.save()

        return Response({'Message': "Orders Sent Successfully"}, status=status.HTTP_200_OK)
    return Response({'Message': "Orders Sent Successfully"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def add_to_cart(request):
    if request.method == 'POST':
        # Create a new cart item using the data from the request
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            # Save the validated data to the database
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # If the data is not valid, return the errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # Return an error response if the request method is not POST
    return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST'])
def remove_from_cart(request):
    if request.method == 'POST':
        # Serialize the request data
        serializer = CartDeleteSerializer(data=request.data)
        if serializer.is_valid():
            # Get the ID of the cart item to be removed
            cart_item_id = serializer.validated_data.get('cart_item_id')

            # Check if the cart item exists
            try:
                cart_item = Cart.objects.get(id=cart_item_id)
            except Cart.DoesNotExist:
                return Response({'error': 'Cart item does not exist'}, status=status.HTTP_404_NOT_FOUND)

            # Delete the cart item from the database
            cart_item.delete()

            return Response({'message': 'Cart item removed successfully'}, status=status.HTTP_200_OK)
        else:
            # Return errors if serializer validation fails
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Return an error response if the request method is not POST
    return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
