# Generated by Django 2.2.4 on 2019-08-22 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190822_0819'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='cart',
            table='Cart',
        ),
        migrations.AlterModelTable(
            name='order',
            table='Order',
        ),
        migrations.AlterModelTable(
            name='user',
            table='User',
        ),
        migrations.AlterModelTable(
            name='variation',
            table='Variation',
        ),
    ]
