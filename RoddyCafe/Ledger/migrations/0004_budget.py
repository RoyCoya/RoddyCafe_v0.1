# Generated by Django 4.0.6 on 2023-03-03 05:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Ledger', '0003_remove_bill_name_bill_remark_alter_bill_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='budget',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='每月预算id')),
                ('year', models.PositiveBigIntegerField(verbose_name='年份')),
                ('month', models.PositiveBigIntegerField(verbose_name='月份')),
                ('budget', models.PositiveIntegerField(verbose_name='该月预算金额')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='所属用户')),
            ],
            options={
                'verbose_name': '每月预算',
                'verbose_name_plural': '每月预算',
                'unique_together': {('user', 'year', 'month')},
            },
        ),
    ]