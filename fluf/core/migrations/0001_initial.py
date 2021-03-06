# Generated by Django 4.0.5 on 2022-06-05 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Animal",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=30)),
                (
                    "sexo",
                    models.CharField(
                        choices=[
                            ("M", "Macho"),
                            ("F", "Fêmea"),
                            ("I", "Indefinido"),
                        ],
                        default="I",
                        max_length=1,
                    ),
                ),
                (
                    "grupo_idade",
                    models.CharField(
                        choices=[
                            ("F", "Filhote"),
                            ("A", "Adulto"),
                            ("I", "Indefinido"),
                        ],
                        default="I",
                        max_length=1,
                    ),
                ),
                ("idade", models.PositiveSmallIntegerField(null=True)),
                (
                    "porte",
                    models.CharField(
                        choices=[
                            ("G", "Grande"),
                            ("M", "Médio"),
                            ("P", "Pequeno"),
                        ],
                        default="P",
                        max_length=1,
                    ),
                ),
                ("raca", models.CharField(max_length=30)),
                ("criado_em", models.DateTimeField(auto_now_add=True)),
                ("atualizado_em", models.DateTimeField(auto_now=True)),
            ],
            options={
                "db_table": "animal",
            },
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                ("titulo", models.CharField(max_length=30)),
                (
                    "animal",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="core.animal",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("I", "Inativo"),
                            ("A", "Ativo"),
                            ("C", "Concluído"),
                        ],
                        default="I",
                        max_length=1,
                    ),
                ),
                ("descricao", models.TextField(max_length=300)),
                ("criado_em", models.DateTimeField(auto_now_add=True)),
                ("atualizado_em", models.DateTimeField(auto_now=True)),
            ],
            options={
                "db_table": "post",
            },
        ),
    ]
