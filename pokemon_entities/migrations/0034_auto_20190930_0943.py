# Generated by Django 2.2.3 on 2019-09-30 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0033_auto_20190930_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Покемон'),
        ),
    ]
