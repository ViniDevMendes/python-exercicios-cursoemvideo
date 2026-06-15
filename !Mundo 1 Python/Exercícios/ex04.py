# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo, e todas as informações possiveis sobre ele.
#              ESSE EU NÃO CONSEGUI FAZER SOZINHO

a = input('Digite algo: ')
print('O tipo desse tipo primitivo é ', type(a))
print('Só tem espaços? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('Está em maísculo? ', a.isupper())
print('Está em minúsculo? ', a.islower())
print('Está capitalizada? ', a.istitle())

# a = objeto