# Generated by Django 4.0.3 on 2022-04-14 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Notebook', '0004_alter_notebook_note_note_directory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notebook_note',
            name='note_title',
        ),
    ]
