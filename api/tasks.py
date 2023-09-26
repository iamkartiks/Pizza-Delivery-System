from celery import shared_task
from datetime import timedelta
from django.utils import timezone
from .models import PizzaOrder

@shared_task
def update_order_status(order_id):
    try:
        order = PizzaOrder.objects.get(pk=order_id)
        current_time = timezone.now()
        
        if order.order_status == 'Placed' and current_time - order.created_at <= timedelta(minutes=1):
            order.order_status = 'Accepted'
        elif order.order_status == 'Accepted' and current_time - order.created_at > timedelta(minutes=1) and current_time - order.created_at <= timedelta(minutes=2):
            order.order_status = 'Preparing'
        elif order.order_status == 'Preparing' and current_time - order.created_at > timedelta(minutes=3) and current_time - order.created_at <= timedelta(minutes=5):
            order.order_status = 'Dispatched'
        elif order.order_status == 'Dispatched' and current_time - order.created_at > timedelta(minutes=5):
            order.order_status = 'Delivered'
        
        order.save()
    except PizzaOrder.DoesNotExist:
        pass
