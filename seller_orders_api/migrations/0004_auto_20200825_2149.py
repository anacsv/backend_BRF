# Generated by Django 3.1 on 2020-08-26 00:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('seller_orders_api', '0003_auto_20200825_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellerorders',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
