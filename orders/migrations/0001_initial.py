# Generated by Django 5.1.4 on 2024-12-24 09:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(db_index=True, editable=False, max_length=8, unique=True)),
                ('quantity', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[('PG', 'Pending'), ('CF', 'Confirmed'), ('SP', 'Shipped'), ('DV', 'Deliverd'), ('CL', 'Cancelled')], default='PG', max_length=15)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]