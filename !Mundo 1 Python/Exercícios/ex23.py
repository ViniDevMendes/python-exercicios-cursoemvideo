# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
# Exemplo:
# Digite um número: 1834
# Unidade: 4 dezena: 3 centena: 8 milhar: 1
#          JEITO DO VÍDEO

num = int(input('Informe um número: '))
n = str(num)
print('Analisando o número {}'.format(num))
print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(n[3], n[2], n[1], n[0]))

# Se o usuário colocar numeros que são apenas 3 digitos ou menos, o sistema vai dar erro pq os 4 digitos não foram usados. 
# Há uma maneira de resolver isso usando Estrutura de Repetição, mas no momento não será usado.
# Sendo assim, irei resolver esse problema de uma forma "matemática de ser".

num = int(input('Digite um número: '))
unidade = num // 1 % 10 
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10
print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(unidade, dezena, centena, milhar))

# Divisão: 1234 / 10 = 123,4
# Divisão inteira: 1234 //10 = 123
# Módulo: 1234 % 10 = 4
# Pra ele descobrir a centena ele faz isso:
# Faz a divisão inteira por 100: 1234 // 100 = 12
# Depois pega o resultado e dividi por 10, mas pega só o resto dessa divisão (que é o módulo): 12 % 10 = 2
# Ou seja, a centena é 2.