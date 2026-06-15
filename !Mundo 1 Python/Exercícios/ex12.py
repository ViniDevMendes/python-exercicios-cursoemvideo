# Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
#        JEITO DO VIDEO

preco = float(input('Qual é o preço do produto? R$'))
novo = preco - (preco * 5 / 100)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preco, novo))


#      JEITO QUE EU FIZ
# valor_original = float(input('Digite o valor do produto sem os 5% de desconto: '))
# preco_novo = valor_original - (valor_original * 5 / 100)
# valor_com_desconto = valor_original * 0.95 # Multiplicado x 0.95 pq eu estou subtraindo 5% do valor original, se fosse 10% de desconto, iria ser valor_original * 0.90
# print('O valor do produto com o desconto é {:.2f} reais'.format(preco_novo))