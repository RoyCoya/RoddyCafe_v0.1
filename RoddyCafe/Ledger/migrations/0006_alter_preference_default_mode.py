# Generated by Django 4.0.6 on 2023-03-03 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ledger', '0005_bill_create_time_preference_default_mode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preference',
            name='default_mode',
            field=models.CharField(choices=[('day', '按日显示'), ('month', '按月显示')], default='day', max_length=50, verbose_name='默认账本模式'),
        ),
    ]
