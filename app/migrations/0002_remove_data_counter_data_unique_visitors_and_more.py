# Generated by Django 4.2.7 on 2023-12-03 07:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='counter',
        ),
        migrations.AddField(
            model_name='data',
            name='unique_visitors',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='data',
            name='visitors',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='visitor',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]