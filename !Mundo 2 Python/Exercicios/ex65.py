# Crie um programa que leia vários números inteiros pelo teclado. 
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores. 

"""

Lógica do enunciado:

1- criar variáveis para armazenar:
- soma dos valores
- quantidade de números digitados
- maior valor
- menor valor

2- iniciar controle de repetição (while True)

3- dentro do loop:
- pedir um número inteiro ao usuário

4- se for o primeiro número:
- definir ele como maior e menor

5- caso não seja o primeiro:
- comparar para atualizar maior e menor

6- somar o valor na variável soma
- aumentar a quantidade de números

7- perguntar se o usuário quer continuar (S/N)

8- se responder "N":
- encerrar o loop

9- no final:
- calcular média (soma / quantidade)
- mostrar maior, menor e média

"""

soma = 0
quantidade = 0
maior = 0
menor = 0
primeiro = True

while True:
    numero = int(input("Digite um número: "))

    soma += numero
    quantidade += 1

    if primeiro:
        maior = numero
        menor = numero
        primeiro = False
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

    continuar = input("Quer continuar? [S/N]: ").strip().upper()

    if continuar == "N":
        break

media = soma / quantidade

print(f"Média dos valores: {media}")
print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")