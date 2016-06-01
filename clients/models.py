from django.db import models

from clients.managers import ClientManager


class Client(models.Model):
    name = models.CharField('Nome', max_length=150)
    email = models.EmailField('E-mail', max_length=170)
    birth_date = models.DateField('Data de nascimento')
    is_active = models.BooleanField('Ativo', default=True)
    is_removed = models.BooleanField('Removido', default=False)

    objects = ClientManager()

    def __unicode__(self):
        return self.name
