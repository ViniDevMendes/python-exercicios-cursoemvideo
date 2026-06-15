# Leia o ano de nascimento de uma pessoa.
# Considerando o ano atual, informe:
# - Se ainda vai se alistar.
# - Se está na hora de se alistar.
# - Se já passou do prazo.
# Mostre também quantos anos faltam ou quantos anos se passaram.

"""

Lógica do enunciado:

1- perguntar o ano que a pessoa nasceu
2- considerando o ano descrito, verificar se ainda vai se alistar, se está na hora ou se já passou
3- idade para se alistar = 18 / ainda vai se alistar < 18 / já pasou > 18
4- se ainda não se alistou, mostrar quantos anos faltam

"""

ano_nascimento = int(input("Digite o ano em que você nasceu: "))
ano_atual = 2026

idade = ano_atual - ano_nascimento

if idade == 18:
    print("Você deve se alistar este ano!")
elif idade < 18:
    print(f"Você ainda vai se alistar, faltam {18 - idade} ano(s)!")
else:
    print(f"Você devia ter se alistado há {idade - 18} ano(s) atrás!")