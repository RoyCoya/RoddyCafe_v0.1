# Generated by Django 4.0.6 on 2023-03-03 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ledger', '0008_bill_classification_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill_classification',
            name='icon',
            field=models.CharField(default='database-fill', max_length=30, verbose_name='分类图标'),
        ),
    ]
