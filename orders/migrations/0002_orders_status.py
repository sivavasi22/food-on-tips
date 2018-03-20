# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='status',
            field=models.CharField(default=2, max_length=1, choices=[(b'N', b'New Order'), (b'C', b'Cooking'), (b'D', b'Done')]),
            preserve_default=False,
        ),
    ]
