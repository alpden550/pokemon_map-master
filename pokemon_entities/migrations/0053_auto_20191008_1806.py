# Generated by Django 2.2.3 on 2019-10-08 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0052_pokemonelementtype_strong_against'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonelementtype',
            name='strong_against',
            field=models.ManyToManyField(blank=True, related_name='pokemon_entities', to='pokemon_entities.PokemonElementType', verbose_name='Силен против'),
        ),
    ]
