# Crie um programa que leia um número inteiro e mostre na tela se ela é PAR ou IMPAR

numero = int(input('Digite um número aleatório: '))
resultado = numero % 2 # o resto da divisão de qualquer numero par por 2 é 0 (% = resto da divisão)
if resultado == 0: # o resto da divisão de qualquer numero impar por 1 (% = resto da divisão)
    print('O número {} é PAR!!'.format(numero))
else:
    print('O número {} é IMPAR!!{}'.format(numero))