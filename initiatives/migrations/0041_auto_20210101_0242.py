# Generated by Django 2.2.11 on 2020-12-31 21:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('initiatives', '0040_auto_20201229_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='initiativecomment',
            name='published_on',
            field=models.DateField(default=datetime.datetime(2020, 12, 31, 21, 12, 50, 411321, tzinfo=utc)),
        ),
    ]
