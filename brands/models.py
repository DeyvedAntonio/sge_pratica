from django.db import models
from app.models import BaseModel


class Brand(BaseModel):

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
        verbose_name = 'marca'
        verbose_name_plural = 'marcas'
