# Generated by Django 4.0.3 on 2022-04-12 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notebook', '0002_alter_notebook_directory_directory_createddate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notebook_note',
            name='note_createDate',
            field=models.DateTimeField(auto_now_add=True, verbose_name='笔记创建时间'),
        ),
        migrations.AlterField(
            model_name='notebook_note',
            name='note_editDate',
            field=models.DateTimeField(auto_now=True, verbose_name='笔记修改时间'),
        ),
    ]