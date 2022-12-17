# Generated by Django 4.0.4 on 2022-06-25 14:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userd', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=50)),
                ('desc', models.TextField(max_length=1000)),
                ('experience', models.CharField(max_length=10)),
                ('worklocation', models.CharField(max_length=100)),
                ('opening', models.IntegerField()),
                ('vacancy', models.IntegerField()),
                ('deadline', models.DateField()),
                ('rec', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userd.jd')),
                ('seek', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]