# Generated by Django 2.2.3 on 2019-09-30 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0023_auto_20190930_0802'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='previous_evolution',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='pokemon_entities.Pokemon'),
            preserve_default=False,
        ),
    ]
