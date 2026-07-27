from django.db import models
from app.models import BaseModel
from brands.models import Brand
from categories.models import Category


class Product(BaseModel):

    title = models.CharField(
        'título',
        max_length=200,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='products',
        related_query_name='product',
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.PROTECT,
        related_name='products',
        related_query_name='product',
    )
    description = models.TextField(
        'descrição',
        null=True,
        blank=True,
    )
    serie_number = models.CharField(
        'número de série',
        max_length=150,
        null=True,
        blank=True,
    )
    cost_price = models.DecimalField(
        'preço de custo',
        max_digits=20,
        decimal_places=2,
    )
    selling_price = models.DecimalField(
        'preço de venda',
        max_digits=20,
        decimal_places=2,
    )
    quantity = models.IntegerField(
        'quantidade',
        default=0,
    )

    class Meta:
        ordering = ['title',]
        verbose_name = 'produto'
        verbose_name_plural = 'produtos'

    def __str__(self):
        return self.title
