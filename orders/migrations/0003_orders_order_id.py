# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_orders_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='order_id',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
