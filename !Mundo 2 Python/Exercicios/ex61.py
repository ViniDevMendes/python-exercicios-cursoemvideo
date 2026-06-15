# Leia o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

primeiro_termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))

cont = 0
termo = primeiro_termo

while cont < 10:
    print(termo, end=" → ")
    termo += razao
    cont += 1