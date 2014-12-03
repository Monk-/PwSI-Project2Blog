# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_user_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
