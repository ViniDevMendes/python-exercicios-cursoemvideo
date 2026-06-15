# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

"""

Enunciado do exercicio

1- mostrar na tela a contagem de 10 a 0
2- no final, mostrar o lançamento dos fogos de artificio

"""

from time import sleep

print("OS FOGOS SERÃO LIBERADOS EM 10 SEGUNDOS!!!")
sleep(1)
for c in range(10, 0, -1):
    sleep(1)
    print(c)
sleep(1)
print("FOGOS LIBERADOS, OLHE PARA O CÉU!!")