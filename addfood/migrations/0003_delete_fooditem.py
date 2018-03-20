# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addfood', '0002_auto_20170329_0753'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FoodItem',
        ),
    ]
