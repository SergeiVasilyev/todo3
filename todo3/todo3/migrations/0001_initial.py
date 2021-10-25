# Generated by Django 3.2.7 on 2021-10-22 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoCat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Todolist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todoitem', models.CharField(max_length=800)),
                ('todoitem_fav', models.BooleanField()),
                ('todoitem_done', models.BooleanField()),
                ('todo_description', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='todo3.todocat', to_field='name')),
            ],
        ),
    ]
