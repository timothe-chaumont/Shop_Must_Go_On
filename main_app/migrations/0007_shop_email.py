# Generated by Django 3.1.2 on 2020-10-31 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_shop_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
