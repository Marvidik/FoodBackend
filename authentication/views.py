from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import PasswordResetToken,OTP,Referal
from .serializer import UserSerializer,ResetPasswordEmailSerializer,PasswordResetConfirmSerializer,OTPSerializer,ConfirmOTPSerializer

from django.core.mail import send_mail
from django.utils import timezone
from .utils import generate_reset_token,generate_otp

from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model, views as auth_views
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect,render

from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.urls import reverse
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes, force_str
import time

from django.conf import settings
from django.http import JsonResponse


# The login API 
@api_view(['POST'])
def login(request):
    #Getting the user from the request data
    user=get_object_or_404(User,username=request.data['username'])
    #Checking if the users password matches 
    if not user.check_password(request.data['password']):
        return Response({"details":"Info Not Found"})
    
    # Getting the users token or generating one if it dosnt exist
    token,created=Token.objects.get_or_create(user=user)
    serializer=UserSerializer(instance=user)
    #Returning the users data and the users token.

    

    # Generate OTP
    otp = generate_otp()

    subject = 'Your OTP REQUEST'
    message = f'Your OTP is: {otp}'
    from_email = 'your_email@example.com'  # Update with your email
    recipient_list = [user.email]

    # Send OTP via Email
    send_mail(subject, message, from_email, recipient_list)

    
    otp_object, otp = OTP.objects.update_or_create(user=user, defaults={'otp': otp})

    
    return Response({"token":token.key,"user":serializer.data})

@api_view(['POST'])
def confirm_otp(request):
    serializer=ConfirmOTPSerializer(data=request.data)

    if serializer.is_valid():
        otp = serializer.validated_data['otp']
        email=serializer.validated_data['email']

        user=User.objects.get(email=email)
        

        # Retrieve the OTP object for the user
        try:
            otp_object = OTP.objects.get(user=user.id)
        except OTP.DoesNotExist:
            return Response({'error': 'OTP not found for the user'}, status=status.HTTP_404_NOT_FOUND)

        # Check if the provided OTP matches the saved OTP
        if otp == otp_object.otp:
            otp_object.delete()
            return Response({'message': 'OTP verified successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Incorrect OTP'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


  

#The registration API
@api_view(['POST'])
def register(request):
    #Getting the data from the user 
    serializer=UserSerializer(data=request.data)
    #Checking if the data is valid and storing the information if it is 
    if serializer.is_valid():
        serializer.save()
        user=User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token=Token.objects.create(user=user)

        return Response({"token":token.key,"user":serializer.data})
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


#Password reset API 
#This sends the password reset token to the user.
@api_view(['POST'])
def password_reset(request):
    serializer = ResetPasswordEmailSerializer(data=request.data)

    #Checking if the data is valid 
    if serializer.is_valid():
        email = serializer.validated_data['email'] 

        user=User.objects.get(email=email)

         # Generate OTP
        otp = generate_otp()

        subject = 'Your OTP REQUEST'
        message = f'Your OTP is: {otp}'
        from_email = 'your_email@example.com'  # Update with your email
        recipient_list = [user.email]

        # Send OTP via Email
        send_mail(subject, message, from_email, recipient_list)

        otp_object, otp = OTP.objects.update_or_create(user=user, defaults={'otp': otp})

    
        return Response({'message': 'Password reset email sent '}, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

#The password reset confirm API
# the view called when the user follows the sent link 
@api_view(['POST'])
def password_reset_confirm(request):
    
    serializer = PasswordResetConfirmSerializer(data=request.data)

    #Checking if the data is valid 
    if serializer.is_valid():
        try:
            email=serializer.validated_data['email']
            #Decoding and getting the user changing the password 
            user = User.objects.get(email=email)

            if user:
                user.set_password(serializer.validated_data['password'])
                user.save()
                return Response({'message': 'Password reset successful'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Error Occured'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

