# Generated by Django 5.0.3 on 2024-03-15 06:33

import ckeditor_uploader.fields
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0002_alter_banner_options_alter_video_options_video_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('subtitle', models.CharField(max_length=255, verbose_name='Подзаголовок')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Контент')),
                ('image', models.ImageField(upload_to='news/', verbose_name='Изображение')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'ordering': ['-date'],
            },
        ),
    ]
