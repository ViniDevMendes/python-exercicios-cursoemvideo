# Crie um programa que leia o nome de uma cidade e diga se ele começa ou não com "SANTO"

cidade = str(input('Digite o nome da cidade em que você mora: ')).strip()
print(cidade[0:5].upper == 'SANTO')