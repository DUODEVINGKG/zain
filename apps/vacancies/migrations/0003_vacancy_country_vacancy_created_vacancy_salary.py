# Generated by Django 5.1.5 on 2025-02-02 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0002_alter_vacancy_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='country',
            field=models.CharField(default=1, max_length=155, verbose_name='Страна'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vacancy',
            name='created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='salary',
            field=models.CharField(default=1, max_length=100, verbose_name='Зарплата'),
            preserve_default=False,
        ),
    ]
