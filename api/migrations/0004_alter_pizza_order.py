# Generated by Django 4.1.7 on 2023-09-26 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_pizza_base_alter_pizza_cheese_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pizzas', to='api.pizzaorder'),
        ),
    ]
