# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

ano_atual = int(input('Ano atual: '))

maiores = 0
menores = 0

for i in range(7):
    nasc = int(input('Ano de nascimento: '))
    idade = ano_atual - nasc

    if idade < 18:
        menores += 1
    else:
        maiores += 1

print(f'Menores de idade: {menores}')
print(f'Maiores de idade: {maiores}')