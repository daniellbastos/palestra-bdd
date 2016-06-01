from django.test import TestCase

from clients.factories import ClientFactory
from clients.models import Client


class ClientTestCase(TestCase):
    def setUp(self):
        ClientFactory.create_batch(is_active=True, is_removed=False, size=5)
        ClientFactory.create_batch(is_active=True, is_removed=True, size=5)
        ClientFactory.create_batch(is_active=False, is_removed=True, size=5)
        ClientFactory.create_batch(is_active=False, is_removed=True, size=5)

    def test_count_active_clients(self):
        self.assertEqual(5, Client.objects.actives().count())

    def test_count_all_clients(self):
        self.assertEqual(20, Client.objects.all().count())
