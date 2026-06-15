# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

# Exemplos:

# APOS A SOPA

# A SACADA DA CASA

# A TORRE DA DERROTA

# O LOBO AMA O BOLO

# ANOTARAM A DATA DA MARATONA

frase = input('Digite uma frase: ').strip().upper()

frase = frase.replace(' ', '')

if frase == frase[::-1]:
    print('É palíndromo')
else:
    print('Não é palíndromo')