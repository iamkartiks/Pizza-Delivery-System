from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class PizzaBase(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return self.name

class Cheese(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return self.name

class Topping(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return self.name
    

class PizzaOrder(models.Model):
    customer = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    order_status = models.CharField(max_length=20)


class Pizza(models.Model):
    base = models.ForeignKey(PizzaBase,null=True, on_delete=models.CASCADE)
    cheese = models.ForeignKey(Cheese, null=True, on_delete=models.CASCADE)
    toppings = models.ManyToManyField(Topping, null=True)
    order = models.ForeignKey(PizzaOrder, null=True, related_name="pizzas",on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=169.00)
