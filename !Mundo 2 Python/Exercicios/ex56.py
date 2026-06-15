# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:

# A média de idade do grupo.

# Qual é o nome do homem mais velho.

# Quantas mulheres têm menos de 20 anos.

soma_idade = 0
maior_idade_homem = 0
nome_velho = ''
mulheres_menos_20 = 0

for i in range(4):
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()

    soma_idade += idade

    if sexo == 'M':
        if idade > maior_idade_homem:
            maior_idade_homem = idade
            nome_velho = nome

    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1

media = soma_idade / 4

print(f'Média de idade: {media}')
print(f'Homem mais velho: {nome_velho}')
print(f'Mulheres com menos de 20: {mulheres_menos_20}')