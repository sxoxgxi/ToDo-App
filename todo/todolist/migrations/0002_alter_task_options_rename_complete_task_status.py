# Generated by Django 4.0.4 on 2022-05-13 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['status']},
        ),
        migrations.RenameField(
            model_name='task',
            old_name='complete',
            new_name='status',
        ),
    ]