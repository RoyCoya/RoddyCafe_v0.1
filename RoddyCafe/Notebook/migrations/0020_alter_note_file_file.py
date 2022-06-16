# Generated by Django 4.0.3 on 2022-06-16 05:50

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('Notebook', '0019_remove_note_file_user_note_file_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note_file',
            name='file',
            field=models.FileField(upload_to=django.db.models.expressions.CombinedExpression(django.db.models.expressions.Value('Notebook/user/'), '+', django.db.models.expressions.F('note__user__id')), verbose_name='文件内容'),
        ),
    ]
