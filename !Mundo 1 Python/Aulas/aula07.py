n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' >>> ')
print('Divisão inteira {} e potência {:.2f}'.format(di, e))

# print('A soma é {}, o produto é {} e a divisão é {:.3f'.format(s, m, d))
# para limitar a quantidade números que saem em 1.3333333333, é só usar p {:.3f] 3 seria a quantidade

