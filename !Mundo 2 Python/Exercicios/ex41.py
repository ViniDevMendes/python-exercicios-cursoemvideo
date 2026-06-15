# Leia o ano de nascimento de um atleta.
# Calcule sua idade.
#
# Classifique-o em uma categoria:
# Mirim
# Infantil
# Júnior
# Sênior
# Master

"""

Lógica do enunciado:

1- perguntar ano de nascimento do atleta
2- calcular a sua idade comparando ano atual (2026)
3- até 9 anos: MIRIM
3- até 14 anos: INFANTIL
4- até 19 anos: JUNIOR
5- até 25 anos: SÊNIOR
6- acima: MASTER

"""

ano_nascimento = int(input("Digite o ano em que você nasceu: "))
ano_atual = 2026

idade = ano_atual - ano_nascimento

if idade <= 9:
    print(f"Você se encaixa na categoria MIRIM, por ter {idade} anos!")
elif idade <= 14:
    print(f"Você se encaixa na categoria INFANTIL, por ter {idade} anos!")
elif idade <= 19:
    print(f"Você se encaixa na categoria JUNIOR, por ter {idade} anos!")
elif idade <= 25:
    print(f"Você se encaixa na categoria SÊNIOR, por ter {idade} anos!")
else:
    print(f"Você se encaixa na categoria MASTER, por ter {idade} anos!")

