from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Order, OrderStatus
from .serializers import CategorySerializer, OrderSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


class OrderList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [AllowAny]

#
# class UserList(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [AllowAny]


# class UserView(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [AllowAny]
#
#     def get_object(self):
#         queryset = self.get_queryset()
#         obj = queryset.get(pk=self.request.query_params.get('id'))
#         return obj


class OrderView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = []

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.get(pk=self.request.query_params.get('id'))
        return obj


# class CreateOrderView(generics.CreateAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#
#     def perform_create(self, serializer):
#         author = User.objects.get_by_natural_key('author')
#         status = OrderStatus.objects.get(pk='status')
#         return serializer.save(author=author, status=status)


# class ContractorList(generics.ListCreateAPIView):
#     queryset = Contractor.objects.all()
#     serializer_class = ContractorSerializer
#     permission_classes = [AllowAny]
#
#
# class RegistrationUserView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = RegistrationUserSerializer
#     permission_classes = [AllowAny]
#
#     def post(self, request, *args, **kwargs):
#         serializer = RegistrationUserSerializer(data=request.data)
#         data = {}
#         if serializer.is_valid():
#             serializer.save()
#             data['response'] = True
#             return Response(data, status=status.HTTP_200_OK)
#         else:
#             data = serializer.errors
#             return Response(data)
#
#
# class RegistrationContractorView(generics.CreateAPIView):
#     queryset = Contractor.objects.all()
#     serializer_class = RegistrationContractorSerializer
#     permission_classes = [AllowAny]
#
#     def post(self, request, *args, **kwargs):
#         serializer = RegistrationContractorSerializer(data=request.data)
#         data = {}
#         if serializer.is_valid():
#             serializer.save()
#             data['response'] = True
#             return Response(data, status=status.HTTP_200_OK)
#         else:
#             data = serializer.errors
#             return Response(data)
