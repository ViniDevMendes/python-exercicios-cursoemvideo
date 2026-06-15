# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última vez

frase = str(input('Digite uma frase aleatória: ')).upper().strip() # upper = maiusculo / strip = tirar espaços da direita e esquerda
print('Nessa frase, a letra A aparecem {} vezes.'.format(frase.count('A'))) # count = conta quantas letras tem em ('')
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1)) # find = procura a letra na frase / +1 pra comecar a contagem no 1 ao inves do 0
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1)) # rfind = procura a letra na direita / +1 pra comecar a contagem no 1 ao inves do 0
