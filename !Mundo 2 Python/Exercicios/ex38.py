# Leia dois números inteiros.
# Informe qual é o maior.
# Se forem iguais, informe isso.

"""

Lógica do enunciado:

1- solicitar um número INTEIRO
2- solicitar outro número INTEIRO
3- calcular se o numero 1 é maior que o numero 2
4- mostrar o maior numero
5- se forem numeros iguais, informar

"""

numero_1 = int(input("Digite um número inteiro: "))
numero_2 = int(input("Digite outro número inteiro: "))

if numero_1 > numero_2:
    print(f"O primeiro número ({numero_1}) é maior que o segundo número ({numero_2}).")
elif numero_2 > numero_1:
    print(f"O segundo número ({numero_2}) é maior que o primeiro número ({numero_1}).")
else:
    print("Os números digitados são iguais.")