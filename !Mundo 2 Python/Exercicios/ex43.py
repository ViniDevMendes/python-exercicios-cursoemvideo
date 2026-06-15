# Leia o peso e a altura de uma pessoa.
# Calcule o IMC.
#
# Classifique o resultado:
# Abaixo do peso
# Peso ideal
# Sobrepeso
# Obesidade
# Obesidade mórbida

"""

Lógica do enunciado:

1- pedir peso e altura
2- calcular o imc (peso / altura ** 2)
3- classificar IMC conforme status do resultado
4- abaixo de 18.5: abaixo do peso
5- entre 18.5 e 25: peso ideal
6- entre 25 até 30: sobrepeso
7- entre 30 e 40: obesidade
8- acima e 40: obesidade mórbida

"""

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f"Seu imc é de {imc:.2f}, se classifica em Abaixo do Peso.")
elif imc <= 25:
    print(f"Seu imc é de {imc:.2f}, se classifica em Peso Ideal.")
elif imc <= 30:
    print(f"Seu imc é de {imc:.2f}, se classifica em Sobrepeso.")
elif imc <= 40:
    print(f"Seu imc é de {imc:.2f}, se classifica em Obesidade.")
else:
    print(f"Seu imc é de {imc:.2f}, se classifica em Obesidade Mórbida.")