from django.test import TestCase
from django.test.client import Client
from django.test.client import RequestFactory
from .views import DjangoSoapService

class ServiceTests(TestCase):
    """SOAP service tests."""

    def test_GET(self):
        service_call = DjangoSoapService()
        self.assertEquals(
            'water',
            'fire',
    )
