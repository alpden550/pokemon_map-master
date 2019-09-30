# Generated by Django 2.2.3 on 2019-09-29 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0014_auto_20190929_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='title_en',
            field=models.CharField(blank=True, default='', help_text='Название покемона на английском', max_length=200),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='title_jp',
            field=models.CharField(blank=True, default='', help_text='Название покемона на японском', max_length=200),
        ),
    ]
