# Generated by Django 4.1.7 on 2023-09-26 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_pizzaorder_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='base',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.pizzabase'),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='cheese',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.cheese'),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.pizzaorder'),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='toppings',
            field=models.ManyToManyField(null=True, to='api.topping'),
        ),
    ]
