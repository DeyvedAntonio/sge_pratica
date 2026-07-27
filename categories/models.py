from django.db import models
from app.models import BaseModel


class Category(BaseModel):
    name = models.CharField(
        'nome',
        max_length=150,
    )
    description = models.TextField(
        'descrição',
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ['name',]
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.name
