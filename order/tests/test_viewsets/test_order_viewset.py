import json

from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status

from django.urls import reverse

from product.factories import CategoryFactory, ProductFactory
from order.factories import UserFactory
from order.models import Order


class TestOrderViewSet(APITestCase):
    client = APIClient()

    def setUp(self):
        self.user = UserFactory()
        self.category = CategoryFactory()
        self.product = ProductFactory(
            title='mouse',
            price=100,
            category=[self.category]
        )

    def test_order(self):
        data = json.dumps({
            'user': self.user.id,
            'products_id': [self.product.id]
        })

        response = self.client.post(
            reverse('order-list', kwargs={'version': 'v1'}),
            data=data,
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        created_order = Order.objects.get(user=self.user)
        self.assertEqual(created_order.product.first().title, 'mouse')
