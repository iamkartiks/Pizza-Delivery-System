from django.urls import path, include
from .views import UsersAPIView, MyTokenObtainPairView, PizzaOrderCreateAPIView
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (PizzaBaseAPIView, ToppingsAPIView, 
                    CheeseAPIView, AddUserAPI, PizzaOrdersAPIView) #UserLoginAPIView, UserRegisterationAPIView # AddUserAPI, 


urlpatterns = [
    path('users/', UsersAPIView.as_view(), name='users-list'),
    path('adduser/', AddUserAPI.as_view(), name='add_user'),
    path('login/', MyTokenObtainPairView.as_view(), name="get-token"),
    path('login/refresh/', TokenRefreshView.as_view()),
    path('baseoptions/', PizzaBaseAPIView.as_view(), name='users-list'),
    path('toppingsoptions/', ToppingsAPIView.as_view(), name='users-list'),
    path('cheeseoptions/', CheeseAPIView.as_view(), name='users-list'),
    path('placeorder/', PizzaOrderCreateAPIView.as_view(), name="place-order"),
    path('allorders/', PizzaOrdersAPIView.as_view(), name="your-orders"),

]