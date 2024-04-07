from rest_framework.serializers import ModelSerializer
from .models import Junks,Foods,Orders


class JunkSerializer(ModelSerializer):

    class Meta:
        model=Junks
        fields="__all__"



class FoodsSerializer(ModelSerializer):


    class Meta:
        model=Foods
        fields="__all__"



class OrderSerializer(ModelSerializer):

    class Meta:
        model=Orders
        fields="__all__"
        