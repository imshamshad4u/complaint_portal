# Generated by Django 4.2 on 2023-06-12 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaint_portal_app', '0007_remove_customer_user_customer_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(default='', max_length=50),
        ),
    ]