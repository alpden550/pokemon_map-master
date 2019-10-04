from django.db import models


class Pokemon(models.Model):
    title = models.CharField('Покемон', max_length=200)
    title_en = models.CharField(
        'Покемон на английском',
        blank=True,
        max_length=200,
        help_text='Название покемона на английском',
    )
    title_jp = models.CharField(
        'Покемон на японском',
        blank=True,
        max_length=200,
        help_text='Название покемона на японском',
    )
    description = models.TextField(
        'Описание', blank=True, help_text='Тут должно быть описание монстра.'
    )
    previous_evolution = models.ForeignKey(
        'self',
        verbose_name='Предыдущая эволюция',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='previous_ev',
    )
    next_evolution = models.ForeignKey(
        'self',
        verbose_name='Следующая эволюция',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='next_ev',
    )
    photo = models.ImageField('Фото', blank=True, null=True)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon, verbose_name='Покемон', on_delete=models.CASCADE, related_name='pokemon_entity'
    )
    lat = models.FloatField('Широта')
    lon = models.FloatField('Долгота')
    appeared_at = models.DateTimeField('Появляется в', null=True, blank=True)
    dissapered_at = models.DateTimeField('Исчезает в', null=True, blank=True)
    level = models.IntegerField('Уровень', default=0)
    health = models.IntegerField('Здоровье', null=True, blank=True)
    strength = models.IntegerField('Сила', null=True, blank=True)
    defence = models.IntegerField('Защита', null=True, blank=True)
    stamina = models.IntegerField('Выносливость', null=True, blank=True)

    def __str__(self):
        return f'Покемон {self.pokemon} {self.id}'
