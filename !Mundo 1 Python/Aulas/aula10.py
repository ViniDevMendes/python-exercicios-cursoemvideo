tempo = int(input('Em que ano o seu carro ou moto foi lançado?: '))
if tempo >= 2020:
    print('Seu veículo está em um bom estado!')
else:
    print('Seu carro está meio veinho hein?')

nome = str(input('Qual o seu nome?: '))
if nome == 'Vinicius':
    print('Que nome lindo você tem!!')
else:
    print('Eu prefito o nome Vinicius :)')
print('Bom dia, {}!'.format(nome))

nota1 = float(input('Digite a primeira nota na matéria de Matemática: '))
nota2 = float(input('Digite a segunda nota na matéria de Matemática: '))
media = (nota1 + nota2) / 2
if media >= 7:
    print('Sua nota na matéria é boa, parabén!!')
else:
    print('Sua nota na matéria foi {}, você precisa estudar mais!'.format(media))