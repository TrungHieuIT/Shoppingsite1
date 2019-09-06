# Generated by Django 2.2.4 on 2019-08-27 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(db_index=True, max_length=150)),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('status', models.SmallIntegerField(choices=[(1, 'Hien thi'), (0, 'An')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Brand',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cate_name', models.CharField(db_index=True, max_length=150)),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.SmallIntegerField(choices=[(1, 'Hien thi'), (0, 'An')])),
            ],
            options={
                'db_table': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_name', models.CharField(db_index=True, max_length=150)),
                ('slug', models.SlugField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('pro_price', models.DecimalField(decimal_places=10, max_digits=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('pro_image', models.ImageField(max_length=255, upload_to='')),
                ('pro_year', models.CharField(max_length=4)),
                ('status', models.SmallIntegerField(choices=[(1, 'Hien thi'), (0, 'An')])),
                ('bra_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Brand')),
                ('cate_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='core.Category')),
            ],
            options={
                'db_table': 'Product',
                'ordering': ('pro_name',),
                'index_together': {('id', 'slug')},
            },
        ),
    ]
