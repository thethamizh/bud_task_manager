# Generated by Django 5.0.7 on 2024-08-18 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_remove_task_completed_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Open', 'Open'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], default='open', max_length=20),
        ),
    ]
