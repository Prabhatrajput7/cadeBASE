# Generated by Django 4.0.3 on 2022-04-22 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='class_teacher',
        ),
        migrations.RemoveField(
            model_name='student',
            name='game',
        ),
        migrations.RemoveField(
            model_name='student',
            name='subject',
        ),
        migrations.DeleteModel(
            name='Sports',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]
