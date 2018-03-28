# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooditem',
            name='choice',
            field=models.CharField(default=datetime.datetime(2017, 4, 1, 9, 13, 2, 57328, tzinfo=utc), max_length=1, choices=[(b'V', b'Veg'), (b'N', b'Non -Veg')]),
            preserve_default=False,
        ),
    ]
