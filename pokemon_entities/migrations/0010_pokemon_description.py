# Generated by Django 2.2.3 on 2019-09-29 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0009_auto_20190929_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='description',
            field=models.TextField(default='Тут должно быть описание монстра.'),
        ),
    ]
