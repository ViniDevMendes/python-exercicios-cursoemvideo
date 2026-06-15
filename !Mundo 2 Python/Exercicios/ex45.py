# Crie um jogo de Pedra, Papel e Tesoura.
#
# O jogador escolhe uma opção.
# O computador escolhe aleatoriamente outra.
#
# Mostre:
# - Escolha do jogador
# - Escolha do computador
# - Resultado da partida
#
# Vitória
# Derrota
# Empate

"""

Lógica do enunciado:

1- definir escolha do bot automaticamente
2- jogador escolhe uma opção
3- após, mostra a escolha do jogador
4- após, mostra a escolha do bot
5- mostrar resultado, sendo vitoria, derrota ou empate

"""

import random

escolha_jogador = int(input(
    "[1] Pedra\n"
    "[2] Papel\n"
    "[3] Tesoura\n"
    "Escolha uma opção: "
))

escolha_bot = random.randint(1, 3)

if escolha_jogador == 1:
    print("Você escolheu Pedra")
elif escolha_jogador == 2:
    print("Você escolheu Papel")
elif escolha_jogador == 3:
    print("Você escolheu Tesoura")

if escolha_bot == 1:
    print("O computador escolheu Pedra")
elif escolha_bot == 2:
    print("O computador escolheu Papel")
elif escolha_bot == 3:
    print("O computador escolheu Tesoura")
    
if escolha_jogador == escolha_bot:
    print("Empate!")
elif escolha_jogador == 1 and escolha_bot == 3:
    print("Vitória!")
elif escolha_jogador == 2 and escolha_bot == 1:
    print("Vitória!")
elif escolha_jogador == 3 and escolha_bot == 2:
    print("Vitória!")
else:
    print("Derrota!")