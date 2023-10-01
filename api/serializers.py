from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.hashers import make_password
from api.models import PizzaBase, Cheese, Topping, Pizza, PizzaOrder
from api.tasks import update_order_status


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        hashed_password = make_password(password)
        user = User.objects.create(password=hashed_password, **validated_data)
        return user
    
    
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['user_id'] = user.id
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data['user_id'] = self.user.id
        return data


class PizzaBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaBase
        fields = ["name"]


class CheeseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cheese
        fields = ["name"]


class ToppingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = ["name"]


class PizzaSerializer(serializers.ModelSerializer):

    base = PizzaBaseSerializer()
    cheese = CheeseSerializer()
    toppings = ToppingsSerializer(many=True)

    class Meta:
        model = Pizza
        fields = ["base" ,"cheese", "toppings"]
    


class PizzaOrderSerializer(serializers.ModelSerializer):
    pizzas = PizzaSerializer(many=True)

    class Meta:
        model = PizzaOrder
        fields = ["customer", "pizzas", "total_price"]

    def create(self, validated_data):
        pizzas_data = validated_data.pop('pizzas')
        request = self.context.get('request')
        total_price = len(pizzas_data) * 69  # Calculate the total price based on the number of pizzas
        order_status = "Placed"
        pizza_order = PizzaOrder.objects.create(customer=request.user, total_price=total_price, order_status=order_status, **validated_data)

        update_order_status.delay(pizza_order.id) 

        for pizza_data in pizzas_data:
            base_data = pizza_data.pop('base', None)
            cheese_data = pizza_data.pop('cheese', None)
            toppings_data = pizza_data.pop('toppings', [])

            pizza = Pizza.objects.create(order=pizza_order, **pizza_data)

            if base_data:
                base, created = PizzaBase.objects.get_or_create(**base_data)
                pizza.base = base
                pizza.save()

            if cheese_data:
                cheese, created = Cheese.objects.get_or_create(**cheese_data)
                pizza.cheese = cheese
                pizza.save()

            for topping_data in toppings_data:
                topping, created = Topping.objects.get_or_create(**topping_data)
                pizza.toppings.add(topping)

        return pizza_order
