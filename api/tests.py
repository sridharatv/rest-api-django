from django.test import TestCase
from .models import Device

from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

# Create your tests here.

class ModelTestCase(TestCase):

    def setUp(self) -> None:
        self.device_name = "Device 1"
        self.device = Device(name=self.device_name)

    def test_model_can_creaet_a_device(self):
        old_count = Device.objects.count()
        self.device.save()
        new_count = Device.objects.count()
        self.assertEqual(old_count, new_count)

class ViewTestCase(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.device_data = {'name': 'New Device'}
        self.response = self.client.post(
            reverse('create'),
            self.device_data,
            format="json")

    def test_api_can_create_a_device(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
