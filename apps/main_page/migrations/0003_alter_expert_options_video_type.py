# Generated by Django 5.0.3 on 2024-04-18 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0002_expert'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expert',
            options={'verbose_name': 'Эксперт', 'verbose_name_plural': 'Эксперты'},
        ),
        migrations.AddField(
            model_name='video',
            name='type',
            field=models.CharField(choices=[('main', 'main'), ('event', 'event')], default='main', max_length=10),
            preserve_default=False,
        ),
    ]