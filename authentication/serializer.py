from django.contrib.auth.models import User
from rest_framework import serializers
from .models import OTP,Referal,Profile


#  user serializer
class UserSerializer(serializers.ModelSerializer):
    referral_name = serializers.CharField(required=False, allow_blank=True)
    class Meta(object):
        model = User
        fields = ( 'id','username', 'email', 'password', 'referral_name')


    def create(self, validated_data):
        referral_name = validated_data.pop('referral_name', None)
        user = User.objects.create(**validated_data)
        
        # Update referral points if referral name is provided
        if referral_name:
            try:
                refer = User.objects.get(username=referral_name)
                if refer:
                    point, created = Referal.objects.get_or_create(user=refer)
                    point.point += 1
                    point.save()
            except User.DoesNotExist:
                pass

        return user


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
    email=serializers.EmailField(min_length=2)
    otp=serializers.CharField()

    class Meta:
        fields=["otp","user"]



#Serializer for the password reset confirm
class PasswordResetConfirmSerializer(serializers.Serializer):
    email=serializers.EmailField(min_length=2)
    password = serializers.CharField(max_length=128)
    confirm_password = serializers.CharField(max_length=128)

    def validate(self, data):
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        # Check if passwords match
        if password != confirm_password:
            raise serializers.ValidationError("Passwords do not match")

        return data
    

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'address']