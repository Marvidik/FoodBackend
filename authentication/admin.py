from django.contrib import admin
from .models import PasswordResetToken,OTP

# Register your models here.
admin.site.register(PasswordResetToken)
admin.site.register(OTP)