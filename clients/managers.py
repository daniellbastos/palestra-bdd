from django.db import models


class ClientManager(models.Manager):
    def actives(self):
        qs = super(ClientManager, self).get_queryset()
        return qs.filter(is_active=True, is_removed=False)
