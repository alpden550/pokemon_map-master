import folium
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.db import connection

from .models import Pokemon, PokemonEntity

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = "https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832&fill=transparent"


def add_pokemon(folium_map, lat, lon, name, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(image_url, icon_size=(50, 50))
    folium.Marker([lat, lon], tooltip=name, icon=icon).add_to(folium_map)


def show_all_pokemons(request):
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    pokemons_entities = PokemonEntity.objects.all().select_related('pokemon')
    pokemons = Pokemon.objects.all()

    for pokemon in pokemons_entities:
        photo_url = (
            request.build_absolute_uri(pokemon.pokemon.photo.url)
            if pokemon.pokemon.photo
            else ''
        )
        if not photo_url:
            continue
        add_pokemon(folium_map, pokemon.lat, pokemon.lon, pokemon.pokemon, photo_url)

    pokemons_on_page = []
    for pokemon in pokemons:
        pokemons_on_page.append(
            {
                'pokemon_id': pokemon.id,
                'img_url': pokemon.photo.url if pokemon.photo else DEFAULT_IMAGE_URL,
                'title_ru': pokemon.title,
            }
        )

    return render(
        request,
        "mainpage.html",
        context={'map': folium_map._repr_html_(), 'pokemons': pokemons_on_page},
    )


def show_pokemon(request, pokemon_id):
    pokemon_entities = PokemonEntity.objects.filter(pokemon=pokemon_id).select_related('pokemon')
    try:
        pokemon_class = pokemon_entities[0].pokemon
    except IndexError:
        return HttpResponseNotFound('<h1>Такой покемон не найден</h1>')

    if pokemon_class.previous_evolution:
        previous_evolution = {
            'pokemon_id': pokemon_class.previous_evolution.id,
            'title_ru': pokemon_class.previous_evolution.title,
            'img_url': pokemon_class.previous_evolution.photo.url,
        }
    else:
        previous_evolution = ''

    if pokemon_class.next_evolution:
        next_evolution = {
            'pokemon_id': pokemon_class.next_evolution.id,
            'title_ru': pokemon_class.next_evolution.title,
            'img_url': pokemon_class.next_evolution.photo.url,
        }
    else:
        next_evolution = ''

    pokemon = {
        'pokemon_id': pokemon_class.id,
        'title_ru': pokemon_class.title,
        'title_en': pokemon_class.title_en,
        'title_jp': pokemon_class.title_jp,
        'img_url': pokemon_class.photo.url if pokemon_class.photo else DEFAULT_IMAGE_URL,
        'description': pokemon_class.description,
        'previous_evolution': previous_evolution,
        'next_evolution': next_evolution,
    }

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemon_entities:
        photo_url = (
            request.build_absolute_uri(pokemon_entity.pokemon.photo.url)
            if pokemon_entity.pokemon.photo
            else DEFAULT_IMAGE_URL
        )
        if not photo_url:
            continue
        add_pokemon(
            folium_map,
            pokemon_entity.lat,
            pokemon_entity.lon,
            pokemon_entity.pokemon.title,
            photo_url,
        )

    return render(
        request,
        "pokemon.html",
        context={'map': folium_map._repr_html_(), 'pokemon': pokemon},
    )
