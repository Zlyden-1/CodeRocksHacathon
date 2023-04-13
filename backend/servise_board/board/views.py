from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Order, OrderStatus, User, Contractor
from .serializers import CategorySerializer, OrderSerializer, ContractorSerializer, UserSerializer, RegistrationUserSerializer, RegistrationContractorSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from rest_framework.decorators import api_view


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


class OrderList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [AllowAny]


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.get(pk=self.request.query_params.get('id'))
        return obj


class OrderView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = []

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.get(pk=self.request.query_params.get('id'))
        return obj


class CreateOrderView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        author = User.objects.get_by_natural_key('author')
        status = OrderStatus.objects.get(pk='status')
        return serializer.save(author=author, status=status)


class ContractorList(generics.ListCreateAPIView):
    queryset = Contractor.objects.all()
    serializer_class = ContractorSerializer
    permission_classes = [AllowAny]


class ContractorView(generics.RetrieveAPIView):
    queryset = Contractor.objects.all()
    serializer_class = ContractorSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.get(pk=self.request.query_params.get('id'))
        return obj


class RegistrationUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationUserSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = RegistrationUserSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = True
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)


class RegistrationContractorView(generics.CreateAPIView):
    queryset = Contractor.objects.all()
    serializer_class = RegistrationContractorSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = RegistrationContractorSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = True
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)


@api_view(['POST'])
def login_user_view(request):
    if request.method == 'POST':
        surname = request.POST.get('surname')
        name = request.POST.get('name')
        patronimic = request.POST.get('patronimic')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        user = authenticate(request, surname=surname, name=name, patronimic=patronimic, email=email,
                            phone_numbe=phone_number, password=password, password2=password2)
        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return JsonResponse({'token': token.key})
        else:
            return JsonResponse({'error': 'Invalid credentials'})

@api_view(['POST'])
def login_contractor_view(request):
    if request.method == 'POST':
        surname = request.POST.get('surname')
        name = request.POST.get('name')
        patronimic = request.POST.get('patronimic')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        contractor = authenticate(request, surname=surname, name=name, patronimic=patronimic, email=email,
                            phone_numbe=phone_number, password=password, password2=password2)
        if contractor is not None:
            login(request, contractor)
            token, created = Token.objects.get_or_create(contractor=contractor)
            return JsonResponse({'token': token.key})
        else:
            return JsonResponse({'error': 'Invalid credentials'})

