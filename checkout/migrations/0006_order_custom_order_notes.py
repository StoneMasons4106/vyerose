# Generated by Django 3.2.5 on 2021-11-23 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_order_sales_tax'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='custom_order_notes',
            field=models.TextField(blank=True, max_length=1024, null=True),
        ),
    ]
