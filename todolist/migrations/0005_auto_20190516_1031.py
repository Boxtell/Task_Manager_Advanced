# Generated by Django 2.1.8 on 2019-05-16 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0004_tasklist_my_tasks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasklist',
            name='my_tasks',
        ),
        migrations.AddField(
            model_name='tasklist',
            name='my_tasks',
            field=models.ManyToManyField(null=True, to='todolist.Task'),
        ),
    ]