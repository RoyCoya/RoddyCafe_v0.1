# Generated by Django 4.1.1 on 2022-09-29 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ranking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rankitem',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='ToolBox/Ranking/%Y/%m/%d/', verbose_name='封面图'),
        ),
    ]