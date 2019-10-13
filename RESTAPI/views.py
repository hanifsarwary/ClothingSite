from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
from rest_framework import generics
from RESTAPI.serializers import ( UserSerializer, OrderSerializer, OrderDetailSerializer, ClothPictureSerializer,
    ClothingUnit
)

from RESTAPI.models import User, ClothingUnit, ClothPicture, Order, OrderDetail


class UserCreateViewSet(generics.ListCreateAPIView):
    
    serializer_class = UserSerializer
    queryset = User.objects.all()