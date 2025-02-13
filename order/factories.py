# import factory
#
# from django.contrib.auth.models import User
# from product.factories import ProductFactory
#
# from order.models import Order
#
#
# class UserFactory(factory.django.DjangoModelFactory):
#     email = factory.Faker('pystr')
#     username = factory.Faker('pystr')
#
#     class Meta:
#         model = User
#
#
# class OrderFactory(factory.django.DjangoModelFactory):
#     user = factory.SubFactory(UserFactory)
#
#     @factory.post_generation
#     def product(self, create, extracted, **kwargs):
#         if not create:
#             return
#
#         if extracted:
#             for product in extracted:
#                 self.product.add(product)


import json
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from django.urls import reverse
from product.factories import CategoryFactory, ProductFactory
# Remover importação de UserFactory
from order.models import Order

class TestOrderViewSet(APITestCase):
    client = APIClient()

    def setUp(self):
        self.category = CategoryFactory()
        self.product = ProductFactory(
            title='mouse',
            price=100,
            category=[self.category]
        )

    def test_order(self):
        data = json.dumps({
            'user': 1,  # Ajuste conforme necessário para seu cenário
            'products_id': [self.product.id]
        })

        response = self.client.post(
            reverse('order-list', kwargs={'version': 'v1'}),
            data=data,
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        created_order = Order.objects.get(user=1)  # Ajuste conforme necessário para seu cenário
        self.assertEqual(created_order.product.first().title, 'mouse')
