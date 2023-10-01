# Create your tests here.
from django.test import TestCase
from django.contrib import auth
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from .models import PizzaOrder, PizzaBase, Topping, Cheese
from .serializers import PizzaOrderSerializer

class AuthTestCase(TestCase):
    """
    test for user authentication
    """
    def setUp(self):
        self.u = User.objects.create_user('test@dom.com', 'test@dom.com', 'pass')
        self.u.is_staff = True
        self.u.is_superuser = True
        self.u.is_active = True
        self.u.save()

    def testLogin(self):
        self.client.login(username='test@dom.com', password='pass')


class AddUserAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('add_user')  # Make sure to replace 'add-user-api' with your actual URL name

    def test_add_user_valid_data(self):
        """
        Test adding a user with valid data.
        """
        valid_payload = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "testpassword"
        }
        response = self.client.post(self.url, valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['username'], valid_payload['username'])
        self.assertEqual(response.data['email'], valid_payload['email'])

    def test_add_user_invalid_data(self):
        """
        Test adding a user with invalid data.
        """
        invalid_payload = {
            "username": "testuser",
            "email": "invalid_email",  # Invalid email format
            "password": "testpassword"
        }
        response = self.client.post(self.url, invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class PizzaOrderCreateAPITest(APITestCase):
    def setUp(self):
        # Create a user for authentication (if required in your view)
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_create_pizza_order(self):
        # Authenticate the user (if required in your view)
        self.client.force_authenticate(user=self.user)

        data = {
            "pizzas": [
                {
                    "price": "169.00",
                    "base": {"name": "Normal"},
                    "cheese": {"name": "Cheddar"},
                    "toppings": [{"name": "Capsicum"}, {"name": "Olives"}, {"name": "Jalapeno"}, {"name": "Sweet Corn"}, {"name": "Baby Corn"}]
                }
            ]
        }
        url = reverse('place-order')
        print('URL:', url)
        response = self.client.post(url, data, format='json')
        print('Response Data:', response.data)

        if response.status_code == status.HTTP_400_BAD_REQUEST:
            print('Validation Errors:', response.data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)