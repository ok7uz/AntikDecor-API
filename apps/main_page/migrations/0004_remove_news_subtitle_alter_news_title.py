# Generated by Django 5.0.3 on 2024-03-15 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0003_news'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='subtitle',
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
    ]
