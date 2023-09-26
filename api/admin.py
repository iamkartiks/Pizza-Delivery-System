from django.contrib import admin
from .models import PizzaOrder,Pizza,PizzaBase,Topping,Cheese
# Register your models here.
admin.site.register(PizzaOrder)
admin.site.register(Pizza)
admin.site.register(PizzaBase)
admin.site.register(Topping)
admin.site.register(Cheese)