# Generated by Django 5.1.5 on 2025-01-29 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_title_photo2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='base',
            name='whatsapp',
            field=models.URLField(blank=True, null=True, verbose_name='Ватсапп'),
        ),
    ]
