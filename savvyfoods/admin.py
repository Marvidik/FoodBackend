from django.contrib import admin
from .models import Junks,Foods,Cart,Restaurant,CartItem
# Register your models here.


admin.site.register(Junks)
admin.site.register(Foods)
admin.site.register(Cart)
admin.site.register(Restaurant)
admin.site.register(CartItem)