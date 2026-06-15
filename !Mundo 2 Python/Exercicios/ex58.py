# Melhore o jogo onde o computador vai pensar em um número entre 0 e 10.
# O jogador vai tentar adivinhar até acertar, mostrando no final
# quantos palpites foram necessários para vencer.

"""
Lógica do enunciado:

1- computador irá escolher automaticamente um número de 0 a 10
2- o jogador vai tentar advinhar o número que o computador escolheu
3- após acertar, mostrar quantas tentativas foram necessárias para acertar

"""

from random import randint
from time import sleep
import os

numero_computador = randint(0, 10)
contagem_tentativas = 0

print("Computador está escolhendo...")
sleep(2)
print("Computador escolheu o número!\nAgora você irá tentar adivinhar!")
sleep(1)

tentar_acertar = int(input("Digite um número de 0 a 10: "))

while tentar_acertar != numero_computador:
    contagem_tentativas += 1

    print("Pensando...")
    sleep(2)
    print(f"Você errou! O computador escolheu outro número (não mostrado aqui).")
    print(f"Você tentou o número: {tentar_acertar}")
    print("Tente novamente em 3 segundos!")
    sleep(3)
    os.system("cls")
    tentar_acertar = int(input("Digite um número de 0 a 10: "))
    
print("Parabéns, você venceu!!!")
print(f"Você precisou de {contagem_tentativas + 1} tentativas.")