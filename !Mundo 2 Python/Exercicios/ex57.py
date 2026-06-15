# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores
# 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

"""
Lógica do enunciado:

1- perguntar o sexo da pessoa
2- se for diferente de 'M' ou 'F', pedir para digitar novamente
3- se for 'M' ou 'F', mostrar mensagem de confirmação

"""
import os

perguntar_sexo = input('Qual o seu sexo? Apenas "M" ou "F": ').lower()

while perguntar_sexo != "m" and perguntar_sexo != "f":
    os.system("cls")
    print("Por gentileza, escolher a opção correta!")
    perguntar_sexo = input('Qual o seu sexo? Apenas "M" ou "F": ').lower()
    if perguntar_sexo == "m":
        os.system("cls")
        print("Obrigado pela resposta, você se identifica como MASCULINO.")
    else:
        os.system("cls")
        print("Obrigado pela resposta, você se identifica como FEMININO.")
