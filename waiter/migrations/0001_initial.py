# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Waiter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('task', models.CharField(max_length=1, choices=[(b'C', b'Clean Table'), (b'S', b'Serve')])),
                ('order_id', models.IntegerField(max_length=3)),
                ('table', models.IntegerField(max_length=5)),
                ('status', models.CharField(max_length=1, choices=[(b'A', b'Attended'), (b'N', b'Not Attended')])),
            ],
        ),
    ]
