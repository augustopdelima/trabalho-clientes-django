from django.db import models

class Cliente(models.Model):
    nome = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        verbose_name='Nome'
    )
    sobrenome = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        verbose_name="Sobrenome"
    )
    cpf = models.CharField(
        max_length=15,
        blank=False,
        null=False,
        verbose_name='CPF'
    )
    genero = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        verbose_name="Gênero"
    )
    civil = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Estado Civil"
    )
    telefone = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        verbose_name="Telefone"
    )
    email = models.EmailField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="E-mail"
    )
    rua = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        verbose_name="Rua"
    )
    numero = models.IntegerField(
        blank=False,
        null=False,
        verbose_name="Número"
    )
    complemento = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Complemento (ex: apto, bloco)"
    )
    bairro = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        verbose_name="Bairro"
    )
    cidade = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        verbose_name="Cidade"
    )
    estado = models.CharField(
        max_length=200,
        blank=False,
        null=False,
        verbose_name="Estado"
    )
    cep = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name="CEP"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Criado em',
    )

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.nome