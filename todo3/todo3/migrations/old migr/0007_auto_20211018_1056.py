# Generated by Django 3.2.7 on 2021-10-18 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo3', '0006_auto_20211018_1044'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todocat',
            old_name='cat_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='todolist',
            old_name='todo_fk',
            new_name='category',
        ),
    ]
