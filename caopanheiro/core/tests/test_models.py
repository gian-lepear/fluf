from core.models import Animal, AnimalGrupoIdade, AnimalPorte, AnimalSexo
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

    def test_model_str(self):
        animal = Animal.objects.get(
            nome="Flufy", idade=8, sexo=AnimalSexo.MACHO
        )
        animal_str = f"{animal.pk}-{animal.nome}-{animal.sexo}-{animal.porte}"
        self.assertEqual(str(animal), animal_str)

    def test_model_repr(self):
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
                "Macho",
                AnimalGrupoIdade.ADULTO,
                8,
                AnimalPorte.PEQUENO,
            ),
            (
                AnimalSexo.MACHO,
                "Adulto",
                8,
                AnimalPorte.PEQUENO,
            ),
            (
                AnimalSexo.MACHO,
                AnimalGrupoIdade.ADULTO,
                9,
                "Pequeno",
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
