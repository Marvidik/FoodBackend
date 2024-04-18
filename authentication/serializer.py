from django.contrib.auth.models import User
from rest_framework import serializers
from .models import OTP


#  user serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ( 'id','username', 'email', 'password')


class OTPSerializer(serializers.ModelSerializer):
    class Meta:
        model=OTP
        fields= ['user','otp']


#Serializer for the reset password email
class ResetPasswordEmailSerializer(serializers.Serializer):
    email=serializers.EmailField(min_length=2)

    class Meta:
        fields=["email"]

#Serializer for the reset password email
class ConfirmOTPSerializer(serializers.Serializer):
    user=serializers.IntegerField()
    otp=serializers.CharField()

    class Meta:
        fields=["otp","user"]



#Serializer for the password reset confirm
class PasswordResetConfirmSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=128)
    confirm_password = serializers.CharField(max_length=128)

    def validate(self, data):
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        # Check if passwords match
        if password != confirm_password:
            raise serializers.ValidationError("Passwords do not match")

        return data
    

