# Generated by Django 5.0.3 on 2024-03-15 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0004_remove_news_subtitle_alter_news_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='banner',
            new_name='banner_image',
        ),
        migrations.AlterField(
            model_name='video',
            name='url',
            field=models.URLField(verbose_name='Ссылка на YouTube'),
        ),
    ]
