# Generated by Django 4.2.3 on 2023-07-13 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0002_alter_task_content'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['done_or_not', '-datetime'], 'verbose_name': 'task', 'verbose_name_plural': 'tasks'},
        ),
    ]
