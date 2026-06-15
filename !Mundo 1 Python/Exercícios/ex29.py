# Escreva um programa que leia a velocidade de um carro. 
# Se ele ultrapasasr 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada KM acima do limite, o limite é 80km/h
#          JEITO DO VIDEO

velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h')
    multa = (velocidade-80) * 7
    print('Você deve pagar uma multa de R${:.2f} reais!'.format(multa))
print('Tenha um bom dia, dirija com segurança!')

#            JEITO QUE EU FIZ

# km = float(input('Digite a quantos km/h você viajou na estrada: '))
# print('Calculando...')
# if km > 80:
#     excesso = km - 80
#     multa = excesso * 7
#     print('Você excedeu o limite de velocidade permitido que é 80km por hora e será multado em R${:.2f} reais.'.format(multa))
# else:
#     print('Você dirigiu dentro do limite de velocidade permitido, parabéns!')

