import uuid
from django.db import models
from django.conf import settings


class BaseModel(models.Model):

    uuid = models.UUIDField(
        unique=True,
        editable=False,
        default=uuid.uuid4,
    )
    created_at = models.DateTimeField(
        'criado em',
        auto_now_add=True,
    )
    modified_at = models.DateTimeField(
        'modificado em',
        auto_now=True,
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        verbose_name='criado por',
        null=True,
        blank=True,
    )
    active = models.BooleanField(
        'ativo',
        default=True,
    )

    class Meta:
        abstract = True
