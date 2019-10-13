from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from RESTAPI.models import ClothingUnit, ClothPicture, Order, OrderDetail, User
from RESTAPI.serializers import (ClothingUnitSerializer, ClothPictureSerializer,
                                 OrderDetailSerializer, OrderSerializer,
                                 UserSerializer)


class UserCreateViewSet(generics.ListCreateAPIView):
    
    serializer_class = UserSerializer
    queryset = User.objects.all()


class GetClothings(generics.ListAPIView):
    
    serializer_class = ClothingUnitSerializer
    
    def get_queryset(self):
        return ClothingUnit.objects.all().order_by('created_at')


class GetPictures(generics.ListAPIView):

    serializer_class = ClothPictureSerializer

    def get_queryset(self):
        return ClothPicture.objects.filter(clothing=self.kwargs['cloth_id'])


class CreateOrderDetail(generics.CreateAPIView):

    serializer_class = OrderDetailSerializer



class GetOrderDetails(generics.ListAPIView):

    serializer_class = OrderDetail

    def get_queryset(self):
        return OrderDetail.objects.filter(order=self.kwargs['order_id'])


class CreateOrder(generics.CreateAPIView):

    serializer_class = OrderSerializer