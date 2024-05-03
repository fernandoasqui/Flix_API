from django.db import models
from actors.models import Actor
from genres.models import Genre

# Após criar a APP começe criando o models


class Movie(models.Model):
    title = models.CharField(max_length=500)
    # on_delete serve para proteger o model e não deixar deletar
    genre = models.ForeignKey(
        Genre, on_delete=models.PROTECT, related_name='movies')
    release_date = models.DateField(null=True, blank=True)
    actors = models.ManyToManyField(Actor, related_name='movies')
    resume = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
