# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_client_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='is_removed',
            field=models.BooleanField(default=False, verbose_name=b'Removido'),
        ),
    ]
