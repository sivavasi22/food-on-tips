# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addfood', '0003_delete_fooditem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_type',
            field=models.CharField(max_length=1, choices=[(b'M', b'Manager'), (b'C', b'Chef'), (b'W', b'Waiter')]),
        ),
    ]
