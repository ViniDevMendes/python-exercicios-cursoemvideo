# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 a 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário vencou ou perdeu

from random import randint
from time import sleep

computador = randint(0, 5) # escolhe aleatoriamente um numero
print('-*-' * 20) # detalhe bonitinho
print('Vou pensar em um número de 0 a 5, tente adivinhar...')
print('-*-' * 20) # detalhe bonitinho
numero = int(input('Em que número eu pensei? '))
print('Processando...')
sleep(3) # espera 3 segundos para mostrar o resultado e dar um resultado de processando
if numero == computador:
    print('Parabéns, você acertou!!')
else:
    print('Você errou, pensei no número {} e não no {}!'.format(computador, numero))

#        JEITO QUE EU FIZ (BEM SIMPLES)
# numero = int(input('Eu pensei em um número, tente adivinhar: '))
# if numero == 2:
#     print('Parabéns, você ACERTOU!!')
# else:
#     print('Infelizmente você errou, tente novamente!!')