from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework import status, permissions, generics, filters
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from .models import PizzaOrder, Pizza, Topping, PizzaBase, Cheese
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import (UserSerializer, MyTokenObtainPairSerializer, PizzaOrderSerializer,
                    ToppingsSerializer, PizzaBaseSerializer, PizzaSerializer, CheeseSerializer) #UserRegisterationSerializer, UserLoginSerializer



class UsersAPIView(APIView):
    """
    Arguments : API View
    Returns : List of all the users from the database
    
    """
   
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many = True)
        return Response(serializer.data)


class AddUserAPI(APIView):
    """
    Arguments : API View, request_data
                request_data = ["username","email","password"]
    Returns : created user data (username & email)
    """
    def post(self, request):    
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)

    
class MyTokenObtainPairView(TokenObtainPairView):
    """
    Arguments : request_data ["username","password"]
    Returns : tokens (refersh , access) and user_id
    """
    serializer_class = MyTokenObtainPairSerializer


class ToppingsAPIView(APIView):
    """
    Arguments : API View
    Returns : List of all the users from the database
    
    """
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, *args, **kwargs):
        toppings = Topping.objects.all()
        serializer = ToppingsSerializer(toppings, many = True)
        return Response(serializer.data)

class CheeseAPIView(APIView):
    """
    Arguments : API View
    Returns : List of all the users from the database
    
    """
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, *args, **kwargs):
        cheese = Cheese.objects.all()
        serializer = CheeseSerializer(cheese, many = True)
        return Response(serializer.data)
    

class PizzaBaseAPIView(APIView):
    """
    Arguments : API View
    Returns : List of all the users from the database
    
    """
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, *args, **kwargs):
        pizza_base = PizzaBase.objects.all()
        serializer = PizzaBaseSerializer(pizza_base, many = True)
        return Response(serializer.data)



class PizzaOrdersAPIView(APIView):

    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, *args, **kwargs):
        orders = PizzaOrder.objects.filter(customer_name=self.request.user)
        serializer =  PizzaOrderSerializer(orders, many=True)
        return Response(serializer.data)



class PizzaOrderViewSet(viewsets.ModelViewSet):
    queryset = PizzaOrder.objects.all()
    serializer_class = PizzaOrderSerializer


class PizzaOrderCreateAPIView(APIView):
    
    def post(self, request, format=None):
        serializer = PizzaOrderSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


