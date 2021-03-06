# Generated by Django 4.0 on 2022-01-29 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_task_options_task_importance_alter_task_task'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'задачу', 'verbose_name_plural': 'Задачи'},
        ),
        migrations.AlterField(
            model_name='task',
            name='importance',
            field=models.PositiveSmallIntegerField(choices=[('Срочно и важно', 'Срочно и важно'), ('Срочно, но не важно', 'Срочно, но не важно'), ('Несрочно, но важно', 'Несрочно, но важно'), ('Несрочно и не важно', 'Несрочно и не важно')], verbose_name='Срочность'),
        ),
    ]
