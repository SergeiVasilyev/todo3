# Generated by Django 3.2.7 on 2021-10-13 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo3', '0003_todolist_todo_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='todo_description',
            field=models.CharField(blank=True, default=None, max_length=1000, null=True),
        ),
    ]
