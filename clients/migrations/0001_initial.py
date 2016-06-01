# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150, verbose_name=b'Nome')),
                ('email', models.EmailField(max_length=170, verbose_name=b'E-mail')),
                ('birth_date', models.DateField(verbose_name=b'Data de nascimento')),
            ],
        ),
    ]
