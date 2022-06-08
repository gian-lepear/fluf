from core.models import (
    Animal,
    AnimalGrupoIdade,
    AnimalPorte,
    AnimalSexo,
    Post,
    PostStatus,
)
from django.core.exceptions import ValidationError
from django.test import TestCase
from parameterized import parameterized


class TestAnimalModel(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        Animal.objects.create(
            nome="Flufy",
            sexo=AnimalSexo.MACHO,
            grupo_idade=AnimalGrupoIdade.ADULTO,
            idade=8,
            porte=AnimalPorte.PEQUENO,
            raca="Yorkshire",
        )

    def test_animal_str(self):
        animal = Animal.objects.get(
            nome="Flufy", idade=8, sexo=AnimalSexo.MACHO
        )
        animal_str = f"{animal.pk}-{animal.nome}-{animal.sexo}-{animal.porte}"
        self.assertEqual(str(animal), animal_str)

    def test_animal_repr(self):
        animal = Animal.objects.get(
            nome="Flufy", idade=8, sexo=AnimalSexo.MACHO
        )
        animal_repr = f"{animal.pk}-{animal.nome}-{animal.sexo}-{animal.porte}"
        self.assertEqual(repr(animal), animal_repr)

    @parameterized.expand(
        [
            (
                AnimalSexo.MACHO,
                AnimalGrupoIdade.ADULTO,
                -1,
                AnimalPorte.PEQUENO,
            ),
            (
                "MA",
                AnimalGrupoIdade.ADULTO,
                8,
                AnimalPorte.PEQUENO,
            ),
            (
                AnimalSexo.MACHO,
                "C",
                8,
                AnimalPorte.PEQUENO,
            ),
            (
                AnimalSexo.MACHO,
                AnimalGrupoIdade.ADULTO,
                9,
                "S",
            ),
        ]
    )
    def test_create_validation_errros(self, sexo, grupo_idade, idade, porte):
        with self.assertRaises(ValidationError):
            Animal.objects.create(
                nome="Doggo",
                sexo=sexo,
                grupo_idade=grupo_idade,
                idade=idade,
                porte=porte,
                raca="Não definido",
            )


class TestPostModel(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.animal = Animal.objects.create(
            nome="Flufy",
            sexo=AnimalSexo.MACHO,
            grupo_idade=AnimalGrupoIdade.ADULTO,
            idade=8,
            porte=AnimalPorte.PEQUENO,
            raca="Yorkshire",
        )
        cls.post = Post.objects.create(
            titulo="Titulo do Post",
            animal=cls.animal,
            status=PostStatus.ATIVO,
            descricao="Descrição do Post Longa" * 10,
        )

    def test_post_str(self):
        post_str = f"{self.post.pk}-{self.post.titulo}-{self.post.status}"
        self.assertEqual(str(self.post), post_str)

    def test_post_repr(self):
        post_repr = f"{self.post.pk}-{self.post.titulo}-{self.post.status}"
        self.assertEqual(repr(self.post), post_repr)

    def test_create_validation_error(self):
        with self.assertRaises(ValidationError):
            Post.objects.create(
                titulo="Titulo do Post",
                animal=self.animal,
                status="X",
                descricao="Descrição do Post Longa" * 10,
            )
