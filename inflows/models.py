from django.db import models
from app.models import BaseModel
from products.models import Product
from supliers.models import Suplier


class Inflow(BaseModel):
    suplier = models.ForeignKey(
        Suplier,
        on_delete=models.PROTECT,
        verbose_name='fornecedor',
        related_name='inflows',
        related_query_name='inflow',
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        verbose_name='produto',
        related_name='inflows',
        related_query_name='inflow',
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
        ordering = ['-created_at']
        verbose_name = 'fornecedor'
        verbose_name_plural = 'fornecedores'

    def __str__(self):
        return str(self.product)
