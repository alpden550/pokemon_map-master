# Generated by Django 2.2.3 on 2019-09-30 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0019_auto_20190930_0752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonentity',
            name='appeared_at',
            field=models.DateTimeField(blank=True, default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='dissapered_at',
            field=models.DateTimeField(blank=True, default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='pokemon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemon_entities.Pokemon'),
        ),
    ]
