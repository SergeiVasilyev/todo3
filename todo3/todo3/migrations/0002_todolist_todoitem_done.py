# Generated by Django 3.2.7 on 2021-10-04 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo3', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='todoitem_done',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]