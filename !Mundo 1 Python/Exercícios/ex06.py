# Crie um algoritimo que leia um número e mostre o seu dobro, triplo e sua raiz quadrada.
#           JEITO DO VIDEO

n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r =  n ** (1/2)
print('O dobro de {} vale {}'.format(n, d))
print('O triplo de {} vale {} \nA raiz quadrada de {} é igual a {:.2f}.'.format(n, t, n, r))

#      OUTRAS POSSIBILIDADES

# n = int(input('Digite um número: '))
# print('O dobro de {} vale {}'.format(n+2))
# print('O triplo de {} vale {} \nA raiz quadrada de {} é igual a {:.2f}.'.format(n, (n+3), n, pow(n. (1/2))))


#          JEITO QUE EU FIZ
# n1 = int(input('Digite um número: '))
# dobro = n1 * 2
# triplo = n1 * 3
# raiz_quadrada = n1 ** (1/2)
# print('O dobro do número {} é: {}'.format(n1, dobro))
# print('O triplo do número {} é: {}'.format(n1, triplo))
# print('A  raiz quadrada do número {} é: {:.2f}'.format(n1, raiz_quadrada))