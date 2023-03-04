# Generated by Django 4.0.6 on 2023-03-03 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ledger', '0004_budget'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='create_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='记录时间'),
        ),
        migrations.AddField(
            model_name='preference',
            name='default_mode',
            field=models.CharField(default='day', max_length=50, verbose_name='默认账本模式'),
        ),
    ]
