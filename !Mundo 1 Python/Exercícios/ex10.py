# Crie um programa que leia quando dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
# Considerando US$1.00 = R$3.27
#         JEITO DO VIDEO

real = float(input('Quanto de dinheiro você tem na carteira? R$'))
dolar = real / 3.27
print('Com R${:.2f} você pode comprar U${:.2f}'.format(real, dolar))


#         JEITO QUE EU FIZ
# valor_real = float(input('Digite quantos reais você tem para comprar em dólar: R$'))
# valor_dolar = 3.27
# valor_conversao = valor_real / valor_dolar
# print('Com R${} você consegue comprar ${:.2f} dólares'.format(valor_real, valor_conversao))