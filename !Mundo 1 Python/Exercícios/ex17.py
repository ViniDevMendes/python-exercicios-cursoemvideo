# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo
# calcule e mostre o comprimento da hipotenusa
#         JEITO DO VIDEO SEM IMPORTAÇÃO

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))

#        JEITO DO VÍDEO COM IMPORTAÇÃO

from math import hypot

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca) # hypot - o calculo da hipotenusa
print('A hipotenusa vai medir {:.2f}'.format(hi))