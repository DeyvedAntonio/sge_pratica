from django.db import models
from app.models import BaseModel
from products.models import Product


class Outflow(BaseModel):

    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name='outflows',
        related_query_name='outflow',
    )
    quantity = models.IntegerField(
        'quantidade',
    )
    description = models.TextField(
        'descrição',
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ['product',]
        verbose_name = 'saída'
        verbose_name_plural = 'saídas'

    def __str__(self):
        return str(self.product)
