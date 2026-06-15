# Desenvolva um programa que pergunte a distância de uma viagem em KM.
# Calcule o preço da passagem, cobrando R$0,50 por KM para viagens de até 200km
# e R$0,45 por KM para viajens maiores
#           JEITO DO VIDEO

distancia = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km.'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('E o preço da sua passagem será de R${:.2f} reais.'.format(preco))

#          JEITO QUE EU FIZ
# distancia = float(input('Quantos kilometros você pretende viajar?: '))
# preco = distancia * 0.50
# preco2 = distancia * 0.45
# if distancia <= 200:
#     print('A passagem para essa viagem irá sair pelo preço de R${:.2f} reais.'.format(preco))
# else:
#     print('A passagem para essa viagem irá sair pelo preço de R${:.2f} reais.'.format(preco2))
# print('Boa viagem!!')