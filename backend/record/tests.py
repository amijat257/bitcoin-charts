from rest_framework import status
from rest_framework.test import APITestCase

from .models import Record


class TestCase(APITestCase):
    def test_top_records(self):
        response = self.client.get('/api/records/top/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
