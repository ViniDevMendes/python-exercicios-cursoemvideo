# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

"""
Lógica do enunciado:

1- pedir 2 valores
2- após ter os valores, mostrar um menu na tela, senndo ele:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
3- deixar cada escolha funcional

"""

import os
from time import sleep

numero_um = int(input("Digite um número INTEIRO: "))
numero_dois = int(input("Digite outro número INTEIRO: "))
os.system("cls")

while True:
    menu = int(input("[1] para SOMAR os números\n[2] para MULTIPLICAR os números\n[3] para MOSTRAR número MAIOR e MENOR\n[4] para adicionar NOVOS NÚMEROS\n[5] para SAIR do programa\nR: "))
    if menu == 1:
        calculo = (numero_um + numero_dois)
        print("Calculando, aguarde...")
        sleep(3)
        os.system("cls")
        print(f"A soma dos números enviados é: {calculo}\n")
    elif menu == 2:
        calculo = (numero_um * numero_dois)
        print("Calculando, aguarde...")
        sleep(3)
        os.system("cls")
        print(f"A multiplicação dos números enviados é: {calculo}\n")
    elif menu == 3:
        if numero_um > numero_dois:
            print("Calculando, aguarde...")
            sleep(3)
            os.system("cls")
            print("O primeiro número é maior que o segundo número!\n")
        elif numero_um < numero_dois:
            print("Calculando, aguarde...")
            sleep(3)
            os.system("cls")
            print("O segundo número é maior que o primeiro número!\n")
        else:
            print("Calculando, aguarde...")
            sleep(3)
            os.system("cls")
            print("Os dois números são iguais!")
    elif menu == 4:
        numero_um = int(input("Digite um número INTEIRO: "))
        numero_dois = int(input("Digite outro número INTEIRO: "))
        os.system("cls")
    elif menu == 5:
        os.system("cls")
        print("Saindo do programa.")
        break