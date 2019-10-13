from RESTAPI.models import User, ClothingUnit, ClothPicture, Order, OrderDetail, Customer
from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'

    
class ClothingUnitSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ClothingUnit
        fields = '__all__'
        

class ClothPictureSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ClothPicture
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):


    class Meta:
        model = Order
        fields = '__all__'


class OrderDetailSerializer(serializers.ModelSerializer):


    class Meta:
        model = OrderDetail
        fields = '__all__'
