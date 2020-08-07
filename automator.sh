#!/bin/bash
# automator.sh

SIAPE='asdfg'
SENHA='hjkl;'

SOURCE="/home/barboza/projects/bitbucket/blueprints/*"
DESTINATION="/home/barboza/projects/github/blueprints_if/"

cp -r $SOURCE $DESTINATION

# purge files
rm geckodriver.log pyvenv.cfg
# purge folders
rm -rf bin lib include share

rm -rf pkgs/__pycache__
rm -rf pkgs/livro/__pycache__
rm -rf pkgs/papel/__pycache__
rm -rf pkgs/plano/__pycache__
rm -rf pkgs/plano/algebra_linear_matematica/__pycache__
rm -rf pkgs/plano/algebra_moderna_matematica/__pycache__
rm -rf pkgs/plano/logica_sistemas_informacao/__pycache__
rm -rf pkgs/plano/variaveis_complexas_matematica/__pycache__
rm -rf pkgs/prova/__pycache__
rm -rf pkgs/scrap/__pycache__
rm -rf pkgs/tempo/__pycache__

rm -f upshot/diarios/*
rm -f upshot/provas/*

cp pkgs/scrap/source_credenciais.py pkgs/scrap/credenciais.py

sed -i "s/seu_siape/$SIAPE/" pkgs/scrap/credenciais.py
sed -i "s/sua_senha/$SENHA/" pkgs/scrap/credenciais.py

rm pkgs/scrap/source_credenciais.py

# calculoiii_fisica
# calculoiii_matematica
# calculoiii_transportes
# matematicaiii_edificacoes
# matematicaiii_telecomunicacoes

echo "Done!"

exit 0
