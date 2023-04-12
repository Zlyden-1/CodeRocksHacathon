from django.shortcuts import render

from models import Category, Order, User
from serializers import CategorySerializer, OrderSerializer, UserSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]

class OrderList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [AllowAny]


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.filter(role=1)
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

