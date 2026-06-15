# Desenvolva um programa que leia o primeiro termo e a razão de uma PA (Progressão Aritmética). No final, mostre os 10 primeiros termos dessa progressão.

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))

for i in range(10):
    termo = primeiro + (i * razao)
    print(termo)