from django.db import models

# Create your models here.

class Produto (models.Model):

    codigo_de_barras = models.CharField(
        max_length=13,
        primary_key=True
    )

    nome_do_produto = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    lote = models.CharField(
        max_length=10,
        null=False,
        blank=False
    )

    ativo = models.BooleanField(
        null=False,
        blank=False,
        default=True
    )


class Estoque (models.Model):

    codigo_de_barras = models.ForeignKey(Produto, on_delete=models.CASCADE)

    quantidade = models.IntegerField(
        null=False,
        blank=False
    )

    dt_fabricacao = models.DateField(
        blank=False,
        null=False
    )

    dt_validade = models.DateField(
        blank=False,
        null=False
    )
    pratileira = models.IntegerField(
        blank=False,
        null=False
    )
