# Escreva um programa que leia um número inteiro qualquer e mostre na tela
# os n primeiros elementos de uma Sequência de Fibonacci.
# Exemplo: 0 → 1 → 1 → 2 → 3 → 5 → 8

n = int(input("Quantos termos da sequência de Fibonacci você quer ver? "))

t1 = 0
t2 = 1
cont = 0

while cont < n:
    print(t1, end=" → ")
    prox = t1 + t2
    t1 = t2
    t2 = prox
    cont += 1