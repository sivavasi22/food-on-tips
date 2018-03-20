# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addfood', '0004_auto_20170419_0409'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='emp_pass',
            field=models.CharField(default=1234, max_length=20),
            preserve_default=False,
        ),
    ]
