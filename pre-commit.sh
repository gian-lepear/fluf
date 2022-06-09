#!/bin/bash

echo "Exportando dev requirements"
poetry export --dev -f  requirements.txt --without-hashes > requirements.dev.txt

echo "Exportando prod requirements"
poetry export -f  requirements.txt --without-hashes > requirements.txt

echo "Removendo pasta do coverage html do projeto"
rm -rf fluf/htmlcov