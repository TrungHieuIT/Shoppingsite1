# Generated by Django 2.2.4 on 2019-09-23 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20190917_0442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='paid',
            field=models.BooleanField(default=False, help_text='Thanh toan hay chua thanh toan'),
        ),
    ]
