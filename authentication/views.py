from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import PasswordResetToken
from .serializer import UserSerializer,ResetPasswordEmailSerializer,PasswordResetConfirmSerializer

from django.core.mail import send_mail
from django.utils import timezone
from .utils import generate_reset_token

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
    return Response({"token":token.key,"user":serializer.data})
  

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
#This sends the password reset link to the user.
@api_view(['POST'])
def password_reset(request):
    serializer = ResetPasswordEmailSerializer(data=request.data)

    #Checking if the data is valid 
    if serializer.is_valid():
        email = serializer.validated_data['email']

        # Generate reset token and timestamp
        token, timestamp = generate_reset_token()


        # Get UID for the user
        UserModel = get_user_model()
        user = UserModel.objects.get(email=email)
        uidb64 = urlsafe_base64_encode(force_bytes(user.pk))

        #converting the timestamp into an integer 
        formatted_timestamp = int(timestamp.timestamp())

        # Store token and timestamp in the database
        PasswordResetToken.objects.create(user=user, token=token, timestamp=formatted_timestamp)
        # Construct password reset URL with UID and token
        reset_url = reverse('password_reset_confirm', kwargs={'uidb64': uidb64, 'token': token})
        reset_link = request.build_absolute_uri(reset_url)

        # Send password reset email
        subject = 'Password Reset Request'
        message = f'Click the link below to reset your password:\n\n{reset_link}'
        from_email = 'ebubeidika@gmail.com' 
        recipient_list = [email]

        send_mail(subject, message, from_email, recipient_list)

    
        return Response({'message': 'Password reset email sent'}, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




#The password reset confirm API
# the view called when the user follows the sent link 
@api_view(['POST'])
def password_reset_confirm(request, uidb64, token):
    
    serializer = PasswordResetConfirmSerializer(data=request.data)

    #Checking if the data is valid 
    if serializer.is_valid():
        try:
            #Decoding and getting the user changing the password 
            user = User.objects.get(pk=force_str(urlsafe_base64_decode(uidb64)))

            # Check token validity
            password_reset = PasswordResetToken.objects.filter(user=user, token=token).first()

            #If the token is valid the password is set and saved 
            if password_reset and password_reset.is_valid():
                user.set_password(serializer.validated_data['password'])
                user.save()
                return Response({'message': 'Password reset successful'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Invalid or expired token'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

