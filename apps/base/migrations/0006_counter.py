# Generated by Django 5.1.5 on 2025-01-29 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_banner_options_alter_base_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partners', models.PositiveIntegerField(verbose_name='Наши партнеры')),
                ('сurrent_employees', models.PositiveIntegerField(verbose_name='Текущие работники')),
                ('free_vacancies', models.PositiveIntegerField(verbose_name='Свободные вакансии')),
                ('happy_clients', models.PositiveIntegerField(verbose_name='Счастливые клиенты')),
            ],
            options={
                'verbose_name': 'Счетчик',
                'verbose_name_plural': 'Счетчик',
            },
        ),
    ]
