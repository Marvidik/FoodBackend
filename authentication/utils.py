# utils.py
from django.utils import timezone
import secrets
import random


#Function to generate token 
def generate_reset_token():
    token = secrets.token_urlsafe(64)  # Generate a random URL-safe token
    timestamp = timezone.now()  # Get the current timestamp
    return token, timestamp



def generate_otp():
    return str(random.randint(1000, 9999))




# def password_reset(request):
#     serializer = ResetPasswordEmailSerializer(data=request.data)

#     #Checking if the data is valid 
#     if serializer.is_valid():
#         email = serializer.validated_data['email']

#         # Generate reset token and timestamp
#         token, timestamp = generate_reset_token()


#         # Get UID for the user
#         UserModel = get_user_model()
#         user = UserModel.objects.get(email=email)
#         uidb64 = urlsafe_base64_encode(force_bytes(user.pk))

#         #converting the timestamp into an integer 
#         formatted_timestamp = int(timestamp.timestamp())

#         # Store token and timestamp in the database
#         PasswordResetToken.objects.create(user=user, token=token, timestamp=formatted_timestamp)
#         # Construct password reset URL with UID and token
#         reset_url = reverse('password_reset_confirm', kwargs={'uidb64': uidb64, 'token': token})
#         reset_link = request.build_absolute_uri(reset_url)

#         # Send password reset email
#         subject = 'Password Reset Request'
#         message = f'Click the link below to reset your password:\n\n{reset_link}'
#         from_email = 'ebubeidika@gmail.com' 
#         recipient_list = [email]

#         send_mail(subject, message, from_email, recipient_list)

    
#         return Response({'message': 'Password reset email sent'}, status=status.HTTP_200_OK)
#     else:
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
