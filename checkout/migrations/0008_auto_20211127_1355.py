# Generated by Django 3.2.5 on 2021-11-27 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_auto_20211126_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='courier',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='tracking_number',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
