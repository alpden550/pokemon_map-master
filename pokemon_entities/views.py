import branca
import folium
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound
from django.shortcuts import render

from .models import Pokemon

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = "https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832&fill=transparent"


def add_pokemon(folium_map, lat, lon, name, pokemon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(image_url, icon_size=(50, 50))
    html = f"""
        <h4>{pokemon.pokemon}</h4>
        <p><b>Уровень</b>: {pokemon.level}<br>
        <b>Здоровье</b>: {pokemon.health}<br>
        <b>Сила</b>: {pokemon.strength}<br>
        <b>Защита</b>: {pokemon.defence}<br>
        <b>Выносливость</b>: {pokemon.stamina}<br>
        </p>
        """
    iframe = branca.element.IFrame(html=html, width=200, height=150)
    popup = folium.Popup(iframe)
    folium.Marker([lat, lon], tooltip=name, icon=icon, popup=popup).add_to(folium_map)


def show_all_pokemons(request):
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    all_pokemons = Pokemon.objects.prefetch_related('pokemon_entities').all()
    all_entities = []
    for pokemon in all_pokemons:
        all_entities.extend(pokemon.pokemon_entities.all())

    for pokemon in all_entities:

        photo_url = (
            request.build_absolute_uri(pokemon.pokemon.photo.url)
            if pokemon.pokemon.photo
            else ''
        )
        if not photo_url:
            continue
        add_pokemon(folium_map, pokemon.lat, pokemon.lon, pokemon.pokemon, pokemon, photo_url)

    pokemons_on_page = []
    for pokemon in all_pokemons:
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
    try:
        pokemon_class = Pokemon.objects.prefetch_related('pokemon_entities').get(id=pokemon_id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound('<h1>Такой покемон не найден</h1>')

    if pokemon_class.previous_evolution:
        previous_evolution = {
            'pokemon_id': pokemon_class.previous_evolution.id,
            'title_ru': pokemon_class.previous_evolution.title,
            'img_url': pokemon_class.previous_evolution.photo.url,
        }
    else:
        previous_evolution = ''

    try:
        next_pokemon = pokemon_class.next_evolutions.all()[0]
        next_evolution = {
            'pokemon_id': next_pokemon.id,
            'title_ru': next_pokemon.title,
            'img_url': next_pokemon.photo.url,
        }
    except IndexError:
        next_evolution = ''

    elements = pokemon_class.elements.all()
    element_types = []
    for element in elements:
        image = element.avatar.url if element.avatar else DEFAULT_IMAGE_URL
        element_types.append({
            'title': element.name,
            'img': image,
            'strong_against': element.strong_against.all()
        })

    pokemon = {
        'pokemon_id': pokemon_class.id,
        'title_ru': pokemon_class.title,
        'title_en': pokemon_class.title_en,
        'title_jp': pokemon_class.title_jp,
        'img_url': pokemon_class.photo.url if pokemon_class.photo else DEFAULT_IMAGE_URL,
        'description': pokemon_class.description,
        'previous_evolution': previous_evolution,
        'next_evolution': next_evolution,
        'element_type': element_types,
    }

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    pokemon_entities = pokemon_class.pokemon_entities.all()
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
            pokemon_entity,
            photo_url,
        )

    return render(
        request,
        "pokemon.html",
        context={'map': folium_map._repr_html_(), 'pokemon': pokemon},
    )
