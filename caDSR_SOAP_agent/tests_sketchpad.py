# Partial fragments of earlier tests which might be useful.  Not currently used by the app.

from django.test import TestCase
from django.test.client import Client

class ServiceTests(TestCase):
    """SOAP service tests."""

    def test_GET(self):
        service_call = DjangoSoapService()
        self.assertEquals(
            'water',
            'fire',
    )