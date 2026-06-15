# Crie um programa que leia um número Real qualquer pelo teclado e mostre a sua porção Inteira
#           JEITO DO VIDEO

from math import trunc

num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num,  trunc(num)))

#           OUTRA MANEIRA

# num = float(input('Digite um valor: '))
# print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num))) - essa opção é sem importar math

#           JEITO QUE EU FIZ
# from math import floor

# real = float(input('Digite um número: '))
# inteiro = floor(real)
# print('O número {} tem a parte Inteira {}'.format(real, inteiro))