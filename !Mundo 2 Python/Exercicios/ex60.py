# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120

n = int(input("Digite um número: "))

resultado = 1

while n > 1:
    resultado *= n
    n -= 1

print(f"Fatorial: {resultado}")