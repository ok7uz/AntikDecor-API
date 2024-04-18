# Generated by Django 5.0.3 on 2024-04-18 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя и фамилия эксперта')),
                ('about', models.TextField(verbose_name='Об эксперте')),
                ('image', models.ImageField(upload_to='experts/', verbose_name='Фотография эксперта')),
            ],
        ),
    ]