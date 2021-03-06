# Generated by Django 2.2.3 on 2019-10-08 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0046_auto_20191005_1731'),
    ]

    operations = [
        migrations.CreateModel(
            name='PokemonElementType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Стихия')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='media/type', verbose_name='Аватар стихии')),
                ('pokemons', models.ManyToManyField(related_name='pokemon_elements', to='pokemon_entities.Pokemon', verbose_name='Покемоны')),
            ],
        ),
    ]
