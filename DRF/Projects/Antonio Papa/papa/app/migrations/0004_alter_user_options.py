# Generated by Django 4.0.4 on 2022-06-05 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_product_alter_user_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-email']},
        ),
    ]
