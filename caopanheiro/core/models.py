from django.db.models import (
    CASCADE,
    CharField,
    CheckConstraint,
    DateTimeField,
    Model,
    OneToOneField,
    PositiveSmallIntegerField,
    Q,
    TextChoices,
    TextField,
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
    criado_em = DateTimeField(auto_now_add=True)
    atualizado_em = DateTimeField(auto_now=True)

    def __repr__(self):
        return f"{self.pk}-{self.nome}-{self.sexo}-{self.porte}"

    def __str__(self):
        return f"{self.pk}-{self.nome}-{self.sexo}-{self.porte}"

    def save(self, *args, **kwargs) -> None:
        self.full_clean()
        return super().save(*args, **kwargs)

    class Meta:
        db_table = "animal"
        constraints = [
            CheckConstraint(
                name="%(app_label)s_%(class)s_sexo_valid",
                check=Q(sexo__in=AnimalSexo.values),
            ),
            CheckConstraint(
                name="%(app_label)s_%(class)s_grupo_idade_valid",
                check=Q(grupo_idade__in=AnimalGrupoIdade.values),
            ),
            CheckConstraint(
                name="%(app_label)s_%(class)s_porte_valid",
                check=Q(porte__in=AnimalPorte.values),
            ),
        ]


class PostStatus(TextChoices):
    INATIVO = "I", _("Inativo")
    ATIVO = "A", _("Ativo")
    CONCLUIDO = "C", _("Concluído")


class Post(Model):
    titulo = CharField(max_length=30, null=False)
    animal = OneToOneField(Animal, on_delete=CASCADE, primary_key=True)
    status = CharField(
        max_length=1,
        choices=PostStatus.choices,
        default=PostStatus.INATIVO,
    )
    descricao = TextField(max_length=300, null=False)
    criado_em = DateTimeField(auto_now_add=True)
    atualizado_em = DateTimeField(auto_now=True)

    def __repr__(self):
        return f"{self.pk}-{self.titulo}-{self.status}"

    def __str__(self):
        return f"{self.pk}-{self.titulo}-{self.status}"

    def save(self, *args, **kwargs) -> None:
        self.full_clean()
        return super().save(*args, **kwargs)

    class Meta:
        db_table = "post"
        constraints = [
            CheckConstraint(
                name="%(app_label)s_%(class)s_status_valid",
                check=Q(status__in=PostStatus.values),
            )
        ]
