# -*- coding: utf-8 -*-
from datetime import datetime

import factory

from clients.models import Client


class ClientFactory(factory.DjangoModelFactory):
    class Meta:
        model = Client

    name = factory.Sequence(lambda n: 'Client #%d' % n)
    email = factory.Sequence(
        lambda n: 'client{0}@example.com'.format(n))
    birth_date = datetime(1990, 06, 15)
    is_active = True
    is_removed = False
