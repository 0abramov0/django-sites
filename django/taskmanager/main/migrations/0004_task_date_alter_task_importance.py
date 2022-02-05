# Generated by Django 4.0 on 2022-01-29 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_task_options_alter_task_importance'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateTimeField(blank=True, default=1, verbose_name='Дата'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='importance',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Срочно и важно'), (2, 'Срочно, но не важно'), (3, 'Несрочно, но важно'), (4, 'Несрочно и не важно')], verbose_name='Срочность'),
        ),
    ]