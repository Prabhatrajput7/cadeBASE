# Generated by Django 4.0.3 on 2022-05-07 07:00

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('changeapp2', '0002_rename_user_name_custom_username_custom_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custom',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
    ]
