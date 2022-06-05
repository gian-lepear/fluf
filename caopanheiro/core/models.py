from django.core.exceptions import ValidationError
from django.db.models import (
    CharField,
    DateTimeField,
    Model,
    PositiveSmallIntegerField,
    TextChoices,
)
from django.utils.translation import gettext_lazy as _


class AnimalSexo(TextChoices):
    MACHO = "M", _("Macho")
    FEMEA = "F", _("Fêmea")
    INDEFINIDO = "I", _("Indefinido")


class AnimalGrupoIdade(TextChoices):
    FILHOTE = "F", _("Filhote")
    ADULTO = "A", _("Adulto")
    INDEFINIDO = "I", _("Indefinido")


class AnimalPorte(TextChoices):
    GRANDE = "G", _("Grande")
    MEDIO = "M", _("Médio")
    PEQUENO = "P", _("Pequeno")


class Animal(Model):
    nome = CharField(max_length=30, null=False)
    sexo = CharField(
        max_length=1,
        choices=AnimalSexo.choices,
        default=AnimalSexo.INDEFINIDO,
    )
    grupo_idade = CharField(
        max_length=1,
        choices=AnimalGrupoIdade.choices,
        default=AnimalGrupoIdade.INDEFINIDO,
    )
    idade = PositiveSmallIntegerField(null=True)
    porte = CharField(
        max_length=1,
        choices=AnimalPorte.choices,
        default=AnimalPorte.PEQUENO,
    )
    raca = CharField(max_length=30, null=False)
    # fotos
    criado_em = DateTimeField(auto_now_add=True)
    atualizado_em = DateTimeField(auto_now=True)

    def __repr__(self):
        return f"{self.pk}-{self.nome}-{self.sexo}-{self.porte}"

    def __str__(self):
        return f"{self.pk}-{self.nome}-{self.sexo}-{self.porte}"

    def save(self, *args, **kwargs) -> None:
        self.full_clean()
        return super().save(*args, **kwargs)
