# Generated by Django 4.0.6 on 2023-03-02 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ledger', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bill',
            options={'verbose_name': '收支记录', 'verbose_name_plural': '收支记录'},
        ),
        migrations.AddField(
            model_name='bill',
            name='value',
            field=models.FloatField(default=0, verbose_name='收支数值'),
        ),
    ]
