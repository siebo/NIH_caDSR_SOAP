# Partial fragments of earlier tests which might be useful.  Not currently used by the app.


class ServiceTests(TestCase):
    """SOAP service tests."""

    def test_GET(self):
        service_call = DjangoSoapService()
        self.assertEquals(
            'water',
            'fire',
    )