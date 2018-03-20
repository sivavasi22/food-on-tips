# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addfood', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('emp_id', models.CharField(max_length=10)),
                ('emp_type', models.CharField(max_length=20)),
                ('emp_firstname', models.CharField(max_length=50)),
                ('emp_lastname', models.CharField(max_length=50)),
                ('emp_hours', models.DecimalField(max_digits=4, decimal_places=2)),
            ],
        ),
        migrations.AddField(
            model_name='fooditem',
            name='food_id',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
