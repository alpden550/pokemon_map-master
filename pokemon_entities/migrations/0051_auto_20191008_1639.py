# Generated by Django 2.2.3 on 2019-10-08 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0050_auto_20191008_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonelementtype',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='type', verbose_name='Аватар стихии'),
        ),
    ]